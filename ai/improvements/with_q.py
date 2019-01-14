from numpy import argmax
from sys import maxsize

from ai.improvement import Improvement


class ImprovementWithQ(Improvement):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """
        A policy improvement method which uses the calculated q-values.
        :param decay_rate: rate at which decay nears its minimum.
        :param decay: starting decay.
        :param decay_max: maximum decay.
        :param decay_min: minimum decay.
        """
        super(ImprovementWithQ, self).__init__(decay_rate, decay, decay_max, decay_min)

    def improve(self):
        for s in range(self.mdp.n_states):
            # action van de max utility value
            a_star = argmax([self.q[s][a] for a in range(self.mdp.n_actions)])

            # we gaan de policy waarde voor elke a in een s updaten
            for a in range(self.mdp.n_actions):
                self.policy[s][a] = 1. * self.decay / self.mdp.n_actions

                # als de action met de max qvalue in een state gelijk is aan action_n
                # dan verhoven we de policy value voor een s|a met 1 - epsilon(t) toe,
                # dit zorgt ervoor dat deze actie meer genomen zal worden
                # hoe verder we gaan hoe minder onze policyvalue verhoogt doordat deze vermindert in de tijd
                if a_star == a:
                    # bij elke stap verlaagd decay waarde adhv decay rate
                    self.policy[s][a] += 1 - self.decay

        return super(ImprovementWithQ, self).improve()
