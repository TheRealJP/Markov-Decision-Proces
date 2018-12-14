from ai.policy_writer import PolicyWriter


class CmdWriter(PolicyWriter):
    def __init__(self):
        pass

    @classmethod
    def write(cls, policy):
        f = '| {0:>3} | {1:>3} | {2:<4.2} |\n'
        output = f.format('S', 'A', 'Pi') + f.format('=', '=', '=').replace(' ', '=')
        output += ''.join([''.join([f.format(s, a, round(policy[s][a], 2)) for a in range(len(policy[s]))])
                          for s in range(len(policy))])
        print output
