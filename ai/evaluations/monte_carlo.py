import numpy

from ai.evaluation import Evaluation


class MonteCarlo(Evaluation):
    def __init__(self, precision, learning_rate):
        """An expansion on the N-step Q-Learning method where N equals the size of the entire episode."""
        super(MonteCarlo, self).__init__(precision, learning_rate)
        self.__P = []

    @property
    def P(self):
        """Returns a list of the buffered Percepts."""
        return self.__P

    def evaluate(self, percept):
        self.P.append(percept)

        if self.P[-1].is_final:
            for p in self.P:
                s = p.prev_state
                a = p.action
                ss = p.new_state
                r = p.reward
                self.q[s][a] -= self.learning_rate * (self.q[s][a] -
                                                      (r + self.mdp.discount * numpy.amax(
                                                          [self.q[ss][aa] for aa in range(self.mdp.n_actions)])))
            self.__P = []
        for s in range(self.mdp.n_states):
            self.v[s] = numpy.amax(self.q[s])
