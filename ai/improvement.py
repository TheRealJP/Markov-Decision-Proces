from math import exp


class Improvement(object):
    """The method used to improve the Agent's policy values."""
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """The method used to improve the Agent's policy values."""
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__t = 0
        self.__decay_rate = decay_rate
        self.__decay = decay
        self.__decay_max = decay_max
        self.__decay_min = decay_min

    @property
    def mdp(self):
        """Returns the Markov Decision Process table, a table that lists the Agent's observations."""
        return self.__mdp

    @property
    def policy(self):
        """Returns the policy used by the agent."""
        return self.__policy

    @property
    def v(self):
        """Returns the v-values list."""
        return self.__v

    @property
    def q(self):
        """Returns the q-values list."""
        return self.__q

    @property
    def t(self):
        """Returns the current iteration: t"""
        return self.__t

    @property
    def decay_rate(self):
        """Returns the decay rate."""
        return self.__decay_rate

    @property
    def decay(self):
        """Returns the current decay value."""
        return self.__decay

    @property
    def decay_max(self):
        """Returns the maximum decay value."""
        return self.__decay_max

    @property
    def decay_min(self):
        """Returns the minimum decay value."""
        return self.__decay_min

    def set(self, mdp, policy, v, q):
        """Initialize the given values."""
        self.__mdp = mdp
        self.__policy = policy
        self.__v = v
        self.__q = q

    def improve(self):
        """Apply the policy improvement."""
        self.__decay = self.decay_min + (self.decay_max - self.decay_min) * exp(-self.decay_rate * self.t)
        self.__t += 1
        return self.__policy
