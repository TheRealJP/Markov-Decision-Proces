from agent_environment import agent_environment
from robotics.visual_writer_optimal_path_csv import VisualWriterOptimalPathCSV


def run():
    env = agent_environment()
    env.fill_optimal_path()

    # first action to start off with
    first_action = env.optimal_path_policy_objects[0].action
    # get the next action after the first in the optimal path
    action = env.step(first_action)

    for _ in range(len(env.optimal_path)):
        # get the next action in the optimal path,
        action = env.step(action)

        # get the amount of radians
        next_rotation_radians = env.next_rotation_radians(action)
        # env.direction_facing = action

        """
        loop over all combinations...check optimal path...least favorite
        """
        print 'next action: ', action, \
            '\tturning this much: {:5} '.format(next_rotation_radians), \
            '\tcurrent direction:', env.direction_facing, \
            '\tcurrent state:', env.current_state

    # show optimal path from csv in gui
    policies = []
    [policies.append(p.action) for p in env.optimal_path_policy_objects]
    VisualWriterOptimalPathCSV.write(policies)


if __name__ == '__main__':
    run()
