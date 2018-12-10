from ai.policy_writer import PolicyWriter


class CsvWriter(PolicyWriter):
    def __init__(self):
        pass

    @classmethod
    def write(cls, policy):
        # Stringify policy
        f = '{0};{1};{2}\n'
        output = ''
        for s in range(len(policy)):
            for a in range(len(policy[s])):
                output += f.format(s, a, round(policy[s][a], 2))

        with open('../policy.csv', 'w') as f:
            [f.write(l) for l in output]
