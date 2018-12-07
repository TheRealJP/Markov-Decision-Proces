class Evaluation(object):
    """The method used to evaluate the Agent's policy values."""
    def __init__(self, precision, learning_rate):
        """The method used to evaluate the Agent's policy values."""
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__precision = precision
        self.__learning_rate = learning_rate

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
    def precision(self):
        """Returns the precision needed for certain evaluation techniques (e.g. Value Iteration)."""
        return self.__precision

    @property
    def learning_rate(self):
        """Returns the learning rate needed for certain evaluation techniques (e.g. Q-Learning)."""
        return self.__learning_rate

    def set(self, mdp, policy, v, q):
        """Initialize the given values."""
        self.__mdp = mdp
        self.__policy = policy
        self.__v = v
        self.__q = q

    def evaluate(self, percept):
        """Apply the policy evaluation."""
        raise NotImplementedError()
