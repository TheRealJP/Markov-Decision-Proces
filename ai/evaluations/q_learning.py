import numpy

from ai.evaluation import Evaluation


class QLearning(Evaluation):
    def evaluate(self, percept):
        s = percept.cur_state
        a = percept.action
        ss = percept.next_state
        self.q[s][a] += self.learning_rate * (self.mdp.r[s][a][ss] + self.mdp.discount *
                                              numpy.amax(
                                                  [self.q[s][a] - self.q[ss][aa] for aa in range(self.mdp.n_actions)]))

        for s in range(self.mdp.n_states):
            self.v[s] = numpy.amax(self.q[s])
