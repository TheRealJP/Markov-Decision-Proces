import numpy

from ai.evaluation import Evaluation


class QLearning(Evaluation):
    def __init__(self, precision, learning_rate):
        """A commonly used method to evaluate policy values that immediately calculates the q- and v-values."""
        super(QLearning, self).__init__(precision, learning_rate)

    def evaluate(self, percept):
        s = percept.prev_state
        a = percept.action
        s_ = percept.new_state
        self.q[s][a] += self.learning_rate * (self.mdp.r[s][a] + self.mdp.discount *
                                              numpy.amax(
                                                  [self.q[s][a] - self.q[s_][aa] for aa in range(self.mdp.n_actions)]))

        for s in range(self.mdp.n_states):
            self.v[s] = numpy.amax(self.q[s])
