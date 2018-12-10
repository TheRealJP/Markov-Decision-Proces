from numpy import argmax
from sys import maxsize

from ai.improvement import Improvement


class ImprovementWithQ(Improvement):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """A policy improvement method which uses the calculated q-values."""
        super(ImprovementWithQ, self).__init__(decay_rate, decay, decay_max, decay_min)

    def improve(self):
        for s in range(self.mdp.n_states):
            a_star = argmax([self.q[s][a] for a in range(self.mdp.n_actions)])

            for a in range(self.mdp.n_actions):
                self.policy[s][a] = 1. * self.decay / self.mdp.n_actions

                if a_star == a:
                    self.policy[s][a] += 1 - self.decay
        return super(ImprovementWithQ, self).improve()
