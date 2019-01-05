class Evaluation(object):
    def __init__(self, precision, learning_rate):
        """
        The method used to evaluate the Agent's policy values.
        :param precision: the precision needed for certain evaluation techniques.
        :param learning_rate: the learning rate needed for certain evaluation techniques.
        """
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__precision = precision
        self.__learning_rate = learning_rate

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
    def precision(self):
        """
        :return: the precision needed for certain evaluation techniques (e.g. Value Iteration).
        """
        return self.__precision

    @property
    def learning_rate(self):
        """
        :return: the learning rate needed for certain evaluation techniques (e.g. Q-Learning).
        """
        return self.__learning_rate

    def set(self, mdp, policy, v, q):
        """
        Initialize the given values.
        :param mdp: agent's MDP.
        :param policy: agent's policy.
        :param v: v-value list.
        :param q: q-value list.
        """
        self.__mdp = mdp
        self.__policy = policy
        self.__v = v
        self.__q = q

    def evaluate(self, percept):
        """Apply the policy evaluation."""
        raise NotImplementedError()
