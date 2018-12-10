import numpy
from sys import maxsize

from ai.evaluation import Evaluation


class ValueIteration(Evaluation):
    def __init__(self, precision, learning_rate):
        """A commonly used method to evaluate policy values that dynamically calculates the v-values."""
        super(ValueIteration, self).__init__(precision, learning_rate)

    def evaluate(self, percept):
        r_max = numpy.amax(self.mdp.r)
        delta = maxsize

        while delta > self.precision * r_max * (1 - self.mdp.discount) / self.mdp.discount:
            delta = 0
            for s in range(self.mdp.n_states):
                u = self.v[s]
                self.q[s] = self.value_function(s)
                self.v[s] = max(self.q[s])
                delta = max(delta, abs(u - self.v[s]))

    def value_function(self, s):
        """Calculates the q-values of a certain state."""
        return [self.policy[s][a] *
                sum([self.mdp.ptsa[s][a][s_] * (self.mdp.r[s][a] + self.mdp.discount * self.v[s_])
                     for s_ in range(self.mdp.n_states)]) for a in range(self.mdp.n_actions)]
