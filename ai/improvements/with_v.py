import numpy

from ai.improvement import Improvement


class ImprovementWithV(Improvement):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """A policy improvement method which uses the calculated v-values."""
        super(ImprovementWithV, self).__init__(decay_rate, decay, decay_max, decay_min)

    def improve(self):
        for s in range(len(self.mdp.ptsa)):
            a_star = numpy.argmax(
                [sum([self.mdp.ptsa[s][a][s_] * (self.mdp.r[s][a] + self.mdp.discount * self.v[s_])
                      for s_ in range(len(self.mdp.ptsa[s][a]))]) for a in range(len(self.mdp.ptsa[s]))])

            for a in range(len(self.mdp.ptsa[s])):
                self.policy[s][a] = 1.0 * self.decay / len(self.mdp.ptsa[s])

                if a_star == a:
                    self.policy[s][a] += 1 - self.decay
        return super(ImprovementWithV, self).improve()
