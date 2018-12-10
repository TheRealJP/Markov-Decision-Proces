from agent_environment import agent_environment as env


def run():
    e = env()
    e.fill_policy()
    for p in e.policy:
        if float(p.probability) > 0.1:
            print p.__str__()


if __name__ == '__main__':
    run()
