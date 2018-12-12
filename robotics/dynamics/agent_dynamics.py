#!/usr/bin/env python

import rospy
import random
import sys
from math import pi
from math import isnan
from math import sqrt

from roslib import message
from nav_msgs.msg import Odometry as odom
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String

from robotics.environment.agent_environment import AgentEnvironment


def dev(x, l):
    n = len(l)
    avg = sum(l) / n
    return (x - avg) ** 2


def std_dev(l):
    n = len(l)
    stddev = 0
    for x in l:
        stddev += dev(x, l)
    return sqrt(stddev / (n - 1))


def avg_minimum(l, n_min):
    dist = n = 0
    stddev = std_dev(l)
    min_dists = [max(l) for _ in range(n_min)]
    max_min_dists = max(min_dists)

    # Compute weighted avg minimum distance, skip NaN
    for point in l:
        if not isnan(point):
            # Get deviation to remove outliers
            d = dev(point, l)
            if (d < 3 * stddev or d > -3 * stddev) and point < max_min_dists:
                min_dists[min_dists.index(max_min_dists)] = point
                max_min_dists = max(min_dists)
        n += 1
    dist = sum(min_dists) / n_min
    rospy.loginfo('dist: %s, nbr of points %s', str(dist), str(n))

    return dist


class Robot:
    def __init__(self, topic, threshold, linear_speed, angular_speed, rate):
        # Init
        rospy.init_node('Noodstop', anonymous=False)
        rospy.on_shutdown(self.shutdown)

        self.__cmd_vel = rospy.Publisher(topic, Twist, queue_size=1)

        # Parameters
        self.__threshold = threshold
        self.__linear_speed = linear_speed
        self.__angular_speed = angular_speed
        self.__move_cmd = Twist()
        self.__rate = rate
        self.__ticks = 0
        self.__current_tick = 0
        self.__turning = False
        rospy.Rate(rate)

        # Subscriptions
        self.__scanner = rospy.Subscriber('/scan', LaserScan, self.set_cmd_vel)
        rospy.loginfo('wait')
        rospy.wait_for_message('/scan', LaserScan)

        # Spin
        rospy.loginfo('spin')
        rospy.spin()

        # Direction & Rotationdata
        self.robot_env = AgentEnvironment(4, 4)
        self.robot_env.fill_optimal_path()

    def set_cmd_vel(self, msg):
        rospy.loginfo('Turning: %s; Ticks: %s / %s',
                      str(self.__turning), str(self.__current_tick), str(self.__ticks))
        move = self.scan(msg)

        # Move forward if possible
        if move and not self.__turning:

            rospy.loginfo('move forward')
            self.__move_cmd.angular.z = 0
            self.__move_cmd.linear.x = self.__linear_speed
            self.__cmd_vel.publish(self.__move_cmd)
        # Else turn
        else:
            rospy.loginfo('turn')
            self.__move_cmd.linear.x = 0
            self.__move_cmd.angular.z = self.__angular_speed
            self.turn()

    #    signal that you have arrived (something like stopped its ticks)
    def turn(self):
        if self.__current_tick < 1:
            angle = pi / 2  # todo replace with radians
            rospy.loginfo('turning %s radians (90 degrees)', angle)
            angular_duration = angle / self.__angular_speed
            self.__ticks = int(angular_duration * self.__rate)
            self.__turning = True
            self.__current_tick = 1
        elif self.__current_tick >= self.__ticks:
            self.__current_tick = 0
            self.__turning = False
        else:
            angle = pi / 2
            rospy.loginfo('turning %s radians (90 degrees)', angle)
            rospy.loginfo('turning at %s radians / s', str(self.__move_cmd.angular.z))
            self.__cmd_vel.publish(self.__move_cmd)
            self.__current_tick += 1

    def scan(self, msg):
        dist = avg_minimum(msg.ranges, len(msg.ranges) / 10)
        return dist > self.__threshold

    def shutdown(self):
        rospy.loginfo('Stopping Roomba')
        self.__cmd_vel.publish(Twist())
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        roomba = Robot('/mobile_base/commands/velocity', .5, .2, .3, 10)
    except:
        rospy.loginfo('Roomba node terminated.')
