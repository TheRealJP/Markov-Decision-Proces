from robotics.dynamics.agent_dynamics import Robot
from robotics.environment.agent_environment import AgentEnvironment
from robotics.policy_writers.visual_writer_optimal_path_csv import VisualWriterOptimalPathCSV

""" testing repositioning location & rotation robot"""


def run():  # todo: implementing this into agent_dynamics class
    env = AgentEnvironment(4, 4)
    env.fill_optimal_path()

    """first action"""
    first_action = env.optimal_path[0].action  # first action to start off with
    next_rotation_radians = env.next_rotation_radians(first_action)

    action = env.step(first_action)  # get the next action after the first in the optimal path

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
    [policies.append(p.action) for p in env.optimal_path]
    VisualWriterOptimalPathCSV.write(policies)


if __name__ == '__main__':
    run()
