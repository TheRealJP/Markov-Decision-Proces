import threading
from concurrent.futures import thread

from agent_environment import agent_environment
from ai.policy_writers.visual_writer import VisualWriter


def run():
    env = agent_environment()
    env.fill_optimal_path()

    for state in range(len(env.optimal_path)):
        # how to ignore non important states

        action = env.action_to_take(state)  # get the next action in the optimal path

        next_rotation = env.next_rotation_radians(action)  # get the amount of radians

        print 'next action: ', action, \
            '\tturning this much: {:5} '.format(next_rotation), \
            '\tcurrent direction:', env.direction_facing, \
            '\tcurrent state:', env.current_state

        # stop loop when you reach reward
        if env.has_reached_reward(True):
            continue

        # set the action as the current direction of the front of the robot
        env.direction_facing = action

    # needs to start seperately
    VisualWriter().write(env.optimal_path)


if __name__ == '__main__':
    run()
