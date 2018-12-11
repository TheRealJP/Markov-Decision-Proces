from agent_environment import agent_environment
from robotics.visual_writer_optimal_path_csv import VisualWriterOptimalPathCSV


def run():
    env = agent_environment()
    env.fill_optimal_path()

    # how to ignore "non important states"
    for state in range(len(env.optimal_path)):
        # get the next action in the optimal path
        action = env.action_to_take(state)
        # get the amount of radians //todo: uncomment radian formula
        next_rotation = env.next_rotation_radians(action)

        """
        loop over all combinations...check optimal path...least favorite
        """
        print 'next action: ', action, \
            '\tturning this much: {:5} '.format(next_rotation), \
            '\tcurrent direction:', env.direction_facing, \
            '\tcurrent state:', env.current_state

        # stop loop when you reach reward
        if env.has_reached_reward(True):
            continue

        # set the action as the current direction of the front of the robot
        env.direction_facing = action

    # show optimal path from csv in gui
    policies = []
    [policies.append(p.action) for p in env.optimal_path_policy_objects]
    VisualWriterOptimalPathCSV.write(policies)


if __name__ == '__main__':
    run()
