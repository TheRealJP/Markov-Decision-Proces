from robotics.environment.agent_environment import AgentEnvironment
from robotics.policy_writers.visual_writer_optimal_path_csv import VisualWriterOptimalPathCSV

""" test implementation for the repositioning & rotation of our robot"""


def print_env_sim(a, rr, df, cs):
    print 'next action: ', a, \
        '\tturning this much: {:5} '.format(rr), \
        '\tcurrent direction:', df, \
        '\tcurrent state:', cs


def run():  # todo: implementing this into agent_dynamics class
    env = AgentEnvironment(4, 4, 15)  # row, column, state where treasure is located
    env.fill_optimal_path()

    action = int(env.optimal_path[0].action)  # first action to start off with
    rot_radians = env.rotate(int(action))
    print_env_sim(action, rot_radians, env.direction_facing, env.current_state)

    for _ in range(len(env.optimal_path)):
        if env.current_state is env.treasure_state:  # todo: replace with opencv bool
            break
        # get the next action and state in the optimal path,
        next_action = env.step(action)
        # get the amount of radians
        rot_radians = env.rotate(int(action))
        action = next_action  # update action with next action
        print_env_sim(action, rot_radians, env.direction_facing, env.current_state)

    # show optimal path from csv file in gui
    policies = []
    [policies.append(p.action) for p in env.optimal_path]
    VisualWriterOptimalPathCSV.write(policies)


if __name__ == '__main__':
    run()
