from math import exp


class Improvement(object):
    def __init__(self, decay_rate, decay, decay_max, decay_min):
        """
        The method used to improve the Agent's policy values.
        :param decay_rate: rate at which decay nears its minimum.
        :param decay: starting decay.
        :param decay_max: maximum decay.
        :param decay_min: minimum decay.
        """
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
        """
        :return: the Markov Decision Process table, a table that lists the Agent's observations.
        """
        return self.__mdp

    @property
    def policy(self):
        """
        :return: the policy used by the agent.
        """
        return self.__policy

    @property
    def v(self):
        """
        :return: the v-values list.
        """
        return self.__v

    @property
    def q(self):
        """
        :return: the q-values list.
        """
        return self.__q

    @property
    def t(self):
        """
        :return: the current iteration.
        """
        return self.__t

    @property
    def decay_rate(self):
        """
        :return: the decay rate.
        """
        return self.__decay_rate

    @property
    def decay(self):
        """
        :return: the current decay value.
        """
        return self.__decay

    @property
    def decay_max(self):
        """
        :return: the maximum decay value.
        """
        return self.__decay_max

    @property
    def decay_min(self):
        """
        :return: the minimum decay value.
        """
        return self.__decay_min

    def set(self, mdp, policy, v, q):
        """
        Initialize the given values.
        :param mdp: agent's MDP.
        :param policy: agent's policy.
        :param v: v-values list.
        :param q: q-values list.
        """
        self.__mdp = mdp
        self.__policy = policy
        self.__v = v
        self.__q = q

    def improve(self):
        """
        Apply the policy improvement.
        :return: the new policy.
        """
        self.__decay = self.decay_min + (self.decay_max - self.decay_min) * exp(-self.decay_rate * self.t)
        self.__t += 1
        return self.__policy
