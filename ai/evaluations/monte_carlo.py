import numpy

from ai.evaluation import Evaluation


class MonteCarlo(Evaluation):
    def __init__(self, precision, learning_rate):
        super(MonteCarlo, self).__init__(precision, learning_rate)
        self.__P = []

    @property
    def P(self):
        return self.__P

    def evaluate(self, percept):
        self.P.append(percept)

        if self.P[-1].isfinal:
            for p in self.P:
                s = p.cur_state
                a = p.action
                ss = p.next_state
                r = p.reward
                self.q[s][a] -= self.learning_rate * (self.q[s][a] -
                                                      (r + self.mdp.discount * numpy.amax(
                                                          [self.q[ss][aa] for aa in range(self.mdp.n_actions)])))
        for s in range(self.mdp.n_states):
            self.v[s] = numpy.amax(self.q[s])
