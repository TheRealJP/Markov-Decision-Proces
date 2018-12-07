from sys import maxsize

from ai.improvement import Improvement


class ImprovementWithQ(Improvement):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """A policy improvement method which uses the calculated q-values."""
        super(ImprovementWithQ, self).__init__(decay_rate, decay, decay_max, decay_min)

    def improve(self):
        for s in range(len(self.mdp.ptsa)):
            a_star = maxsize

            for a in range(len(self.mdp.ptsa[s])):
                sum_a = self.q[s][a]
                if a_star < sum_a:
                    a_star = a

            for a in range(len(self.mdp.ptsa[s])):
                self.policy[s][a] = 1.0 * self.decay / len(self.mdp.ptsa[s])

                if a_star == a:
                    self.policy[s][a] += 1 - self.decay
        return super(ImprovementWithQ, self).improve()
