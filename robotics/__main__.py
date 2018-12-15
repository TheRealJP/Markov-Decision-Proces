import sys

from beginner_tutorials.scripts.agent_environment import AgentEnvironment
from robotics.policy_writers.visual_writer_optimal_path_csv import VisualWriterOptimalPathCSV

""" test implementation for the repositioning & rotation of our robot"""


# roslaunch turtlebot_gazebo turtlebot_world.launch
# world_file:=/home/jonathanpeers/jonathanp627@gmail.com/Informatica/INF3/Robotics_AI_Project_2018-2019/sim.world

def print_env_sim(a, rr, df, cs):
    print'current direction:', df, \
        '\tcurrent state: {:5}'.format(cs), \
        '\tnext direction: ', a, \
        '\tturning this much: ', rr


def run():  # todo: implementing this into agent_dynamics class
    # row, column, state where treasure is located
    env = AgentEnvironment(4, 4, 15)
    env.fill_optimal_path()

    # starting setup
    action = int(env.optimal_path[0].action)  # first action to start off with
    rot_radians = env.rotate(int(action))
    print_env_sim(action, rot_radians, env.direction_facing, env.current_state)
    # env.direction_facing = action

    for _ in range(len(env.optimal_path)):
        if env.current_state is env.treasure_state:  # todo: replace with opencv bool
            break

        # get the amount of radians
        rot_radians = env.rotate(int(action))
        # get the next action and state in the optimal path,
        next_action = env.step(action)
        print_env_sim(next_action, rot_radians, env.direction_facing, env.current_state)

        # update action with next action
        action = next_action

    # show optimal path from csv file in gui
    policies = []
    [policies.append(p.action) for p in env.optimal_path]
    VisualWriterOptimalPathCSV.write(policies)


if __name__ == '__main__':
    for i in range(len(sys.path)):
        print sys.path[i]

    run()
