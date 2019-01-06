from datetime import datetime

from ai.policy_writer import PolicyWriter


class CsvWriter(PolicyWriter):
    def __init__(self):
        pass

    @classmethod
    def write(cls, policy):
        # Stringify policy
        f = '{0},{1},{2}\n'
        output = ''.join([''.join([f.format(s, a, round(policy[s][a], 2)) for a in range(len(policy[s]))])
                          for s in range(len(policy))])

        now = datetime.today()
        now = now.strftime("%d_%m_%Y-%H:%M:%S")
        with open('../files/policy' + now + '.csv', 'w') as f:
            [f.write(l) for l in output]
