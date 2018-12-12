import csv

import numpy

from ai.policy import Policy


class AgentEnvironment:

    def __init__(self, row, column, treasure_state):
        self.row = row
        self.column = column
        self.treasure_state = treasure_state
        self.current_state = 0
        self.optimal_path = []
        self.direction_facing = 2  # starting direction of robot

    """
    robot puts a step in the given action/direction
    change state and face_direction
    """

    def step(self, action):
        # check for limit, todo: stop when reward boolean is true
        if self.current_state <= (len(self.optimal_path) - 1):
            # get the next state & action by moving the robot
            next_action, next_state = self.move_robot(action)
            self.current_state = next_state  # update state

            return int(next_action)

    """move in the optimal path array"""

    def move_robot(self, direction):
        if self.current_state >= len(self.optimal_path) - 1:
            return 0, 0

        # "reposition" index/status of robot
        if direction == 0:  # left
            index = self.current_state - 1
        elif direction == 1:  # down
            index = self.current_state + self.row  # length of row
        elif direction == 2:  # right
            index = self.current_state + 1
        elif direction == 3:  # up
            index = self.current_state - self.row
        else:
            index = 0

        # set the action as the current direction of the front of the robot
        # self.direction_facing = direction

        # get the action and state at the next position
        # if its smaller
        next_action = self.optimal_path[index if index >= 0 else self.current_state].action
        next_state = self.optimal_path[index if index >= 0 else self.current_state].state
        return int(next_action), int(next_state)

    """returns radians"""

    def rotate(self, new_direction):
        # assure that there still are next states
        if self.current_state >= len(self.optimal_path) - 1:
            return 0

        pos_rotation = False  # negative rotation
        amount_of_turns = new_direction - self.direction_facing

        if amount_of_turns is 0:
            return 0

        # change to positive rotation
        if amount_of_turns > 0:
            pos_rotation = True  # positive rotation

        # if self.current_state is not 0:
        self.direction_facing = new_direction

        global target_degrees
        abs_aot = abs(amount_of_turns)
        if abs_aot is 1:
            target_degrees = 90 if pos_rotation else -90
        elif abs_aot is 2:
            target_degrees = 180 if pos_rotation else -180
        elif abs_aot is 3:
            target_degrees = 270 if pos_rotation else -270

        return target_degrees  # * math.pi / 180 #todo: uncomment to turn on radians

    """
    opencv gives back boolean and tells robot to stop
    if opencv sees the endgoal AND the next action is towards the last state then stop
    """

    def has_reached_reward(self, reward_reached):
        # self.reward_reached = reward_reached and self.next_state == len(self.optimal_path) - 1
        return reward_reached

    """extract the optimal path"""

    def fill_optimal_path(self):
        with open('../voorbeeld_policy.csv', 'r') as f:
            reader = csv.reader(f)
            for file_row in reader:
                if float(file_row[2]) > 0.5:
                    p = Policy(file_row[0], file_row[1], file_row[2])
                    self.optimal_path.append(p)
