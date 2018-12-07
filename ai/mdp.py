import numpy as np


class MDP(object):
    """Markov Decision Process: table of data observed by the Agent."""
    def __init__(self, n_states, n_actions, discount):
        """Markov Decision Process: table of data observed by the Agent."""
        self.__n_states = n_states
        self.__n_actions = n_actions
        self.__r = np.array([[.0 for _ in range(n_actions)] for _ in range(n_states)])
        self.__nsa = np.array([[0 for _ in range(n_actions)] for _ in range(n_states)])
        self.__ntsa = np.array([[[0 for _ in range(n_states)] for _ in range(n_actions)] for _ in range(n_states)])
        self.__ptsa = np.array([[[.0 for _ in range(n_states)] for _ in range(n_actions)] for _ in range(n_states)])
        self.__discount = discount

    @property
    def n_states(self):
        """Returns the amount of states in the Environment."""
        return self.__n_states

    @property
    def n_actions(self):
        """Returns the amount of actions in the Environment."""
        return self.__n_actions

    @property
    def r(self):
        """Returns the list of rewards per state-action in the Environment."""
        return self.__r

    @property
    def nsa(self):
        """Returns the state-action frequencies."""
        return self.__nsa

    @property
    def ntsa(self):
        """Returns the state-action-nextstate frequencies."""
        return self.__ntsa

    @property
    def ptsa(self):
        """Returns the state-action-nextstate possibilities."""
        return self.__ptsa

    @property
    def discount(self):
        """Returns the return discount."""
        return self.__discount

    def update(self, percept):
        """Update the MDP table based on the given Percept."""
        s = percept.prev_state
        a = percept.action
        s_ = percept.new_state

        self.r[s][a] = percept.reward
        self.nsa[s][a] += 1
        self.ntsa[s][a][s_] += 1
        self.ptsa[s][a][s_] = 1.0 * self.ntsa[s][a][s_] / self.nsa[s][a]

    def __str__(self):
        f = '| {0:>2} | {1:>2} | {2:>2} | {3:>4.4} | {4:>4.4} |\n'
        output = f.format('S', 'A', 'S\'', 'P', 'R')
        output += f.format('=', '=', '=', '=', '=').replace(' ', '=')

        s = 0
        for states in self.ptsa:
            a = 0
            for actions in states:
                ss = 0
                for probability in actions:
                    if probability > 0:
                        output += f.format(str(s), str(a), str(ss), str(probability), str(self.r[s][a][ss]))
                    ss += 1
                a += 1
            s += 1
        return output
