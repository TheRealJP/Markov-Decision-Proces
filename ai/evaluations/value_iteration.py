import numpy
from sys import maxsize

from ai.evaluation import Evaluation


# DP solves for the optimal policy or value function by recursion.
# It requires knowledge of the markov decision process (MDP) or a model of the world
# so that the recursions can be carried out.
# It is typically lumped under "planning" rather than "learning",
# in that you already know the MDP, and just need to figure out what to do (optimally).

# TD is model-free: it doesn't require knowledge of a model of the world.
# It is iterative, and simulation based, and learns by bootstrapping, i.e.

class ValueIteration(Evaluation):
    def __init__(self, precision, learning_rate):
        """
        A commonly used method to evaluate policy values that dynamically calculates the v-values.
        :param precision: precision used for comparing float numbers.
        :param learning_rate: not used in this method.
        """
        super(ValueIteration, self).__init__(precision, learning_rate)

    def evaluate(self, percept):
        r_max = numpy.amax(self.mdp.r)  # max reward in mdp
        delta = maxsize  # max verschil in waarden tss 2 stappen

        while delta > self.precision * r_max * (1 - self.mdp.discount) / self.mdp.discount:
            delta = 0
            for s in range(self.mdp.n_states):
                # old utility value
                u = self.v[s]

                # q values
                self.q[s] = self.value_function(s)
                # new utility value (max(q_values))
                self.v[s] = max(self.q[s])

                # delta updaten
                # max(old_delta, abs(v(s) - v(s')))zzzzz
                delta = max(delta, abs(u - self.v[s]))

    # q values
    def value_function(self, s):
        """
        Calculates the q-values of a certain state.
        :param s: the state of which you need the utility values.
        :return: list of utility values per action for the given state.
        """
        return [self.policy[s][a] * sum([self.mdp.ptsa[s][a][s_] * (self.mdp.r[s][a] + self.mdp.discount * self.v[s_])
                                         for s_ in range(self.mdp.n_states)]) for a in range(self.mdp.n_actions)]
