from numpy import amax

from ai.evaluation import Evaluation


# leert uit andere onvolledige episodes
# TD learning is model vrij, geen kennis van mdp transities of rewards


class QLearning(Evaluation):
    def __init__(self, precision, learning_rate):
        """
        A commonly used method to evaluate policy values that immediately calculates the q- and v-values.
        :param precision: not used in this method.
        :param learning_rate: rate at which the utility values improve.
        """
        super(QLearning, self).__init__(precision, learning_rate)

    def evaluate(self, percept):
        s = percept.prev_state
        a = percept.action
        s_ = percept.new_state

        # learning rate beinvloed hoeveel de utility waarde voor een bepaalde state/action combinatie stijgt
        # delta max(huidige utility - volgende utility) * discount + reward[s][a]) * lr = v.pi(s)
        self.q[s][a] += self.learning_rate * (self.mdp.r[s][a] + self.mdp.discount *
                                              amax([self.q[s_][a_] - self.q[s][a]
                                                    for a_ in range(self.mdp.n_actions)]))

        # v(s) = amax(R(s,a) + y * V(s'))
        # bepaalde state heeft een bepaalde value die aantoont dat het belangrijk is om daar naartoe te gaan
        # genoteerd als v(s) (utility value)
        for s in range(self.mdp.n_states):
            self.v[s] = amax(self.q[s])
