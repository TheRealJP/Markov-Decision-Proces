import numpy
from sys import maxsize

from ai.evaluation import Evaluation


class ValueIteration(Evaluation):
    def evaluate(self, percept):
        r_max = numpy.amax(self.mdp.r)
        delta = maxsize

        while delta > self.precision * r_max * (1 - self.mdp.discount) / self.mdp.discount:
            delta = 0
            for s in range(self.mdp.n_states):
                u = self.v[s]
                self.v[s] = numpy.amax(self.value_function(s))
                delta = max(delta, abs(u - self.v[s]))

    def value_function(self, s):
        return [self.policy[s][a] *
                sum([self.mdp.ptsa[s][a][ss] * (self.mdp.r[s][a][ss] + self.mdp.discount * self.v[ss])
                     for ss in range(self.mdp.n_states)]) for a in range(self.mdp.n_actions)]
