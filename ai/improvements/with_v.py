import numpy

from ai.improvement import Improvement


class ImprovementWithV(Improvement):
    def improve(self):
        for s in range(len(self.mdp.ptsa)):
            a_star = numpy.argmax(
                [sum([self.mdp.ptsa[s][a][ss] * (self.mdp.r[s][a][ss] + self.mdp.discount * self.v[ss])
                      for ss in range(len(self.mdp.ptsa[s][a]))]) for a in range(len(self.mdp.ptsa[s]))])

            for a in range(len(self.mdp.ptsa[s])):
                self.policy[s][a] = 1.0 * self.decay / len(self.mdp.ptsa[s])

                if a_star == a:
                    self.policy[s][a] += 1 - self.decay
        return super(ImprovementWithV, self).improve()
