from numpy import argmax

from ai.improvement import Improvement


class ImprovementWithV(Improvement):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """
        A policy improvement method which uses the calculated v-values.
        :param decay_rate: rate at which decay nears its minimum.
        :param decay: starting decay.
        :param decay_max: maximum decay.
        :param decay_min: minimum decay.
        """
        super(ImprovementWithV, self).__init__(decay_rate, decay, decay_max, decay_min)

    def improve(self):

        for s in range(self.mdp.n_states):
            # action van de grootste som die bestaat uit elementen van
            # ptsa * v(s)
            a_star = argmax(
                [sum([self.mdp.ptsa[s][a][s_] * (self.mdp.r[s][a] + self.mdp.discount * self.v[s_])
                      for s_ in range(self.mdp.n_states)]) for a in range(self.mdp.n_actions)])

            for a in range(self.mdp.n_actions):
                self.policy[s][a] = 1. * self.decay / self.mdp.n_actions

                if a_star == a:
                    self.policy[s][a] += 1 - self.decay
        return super(ImprovementWithV, self).improve()
