from agent_environment import agent_environment


def run():
    env = agent_environment()
    env.fill_optimal_path()

    for _ in env.optimal_path:
        action = env.action_to_take()
        next_rotation = env.next_rotation_radians(action)

        print 'next action: ', action, \
            'turning this much: ', next_rotation, \
            'current direction:', env.direction_facing


if __name__ == '__main__':
    run()
