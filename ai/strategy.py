from ai.mdp import MDP


class Strategy(object):
    def __init__(self, evaluation, improvement, discount):
        """
        The strategy used by the Agent to evaluate and improve the policy values.
        :param evaluation: the evaluation method to use.
        :param improvement: the improvement method to use.
        :param discount: the return discount.
        """
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__evaluation = evaluation
        self.__improvement = improvement
        self.__discount = discount

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
    def evaluation(self):
        """
        :return: the evaluation method.
        """
        return self.__evaluation

    @property
    def improvement(self):
        """
        :return: the improvement method.
        """
        return self.__improvement

    @property
    def discount(self):
        """
        :return: the return discount.
        """
        return self.__discount

    def set(self, n_states, n_actions):
        """
        Initialize the given values.
        :param n_states: amount of states.
        :param n_actions: amount of actions.
        """
        self.__mdp = MDP(n_states, n_actions, self.discount)
        self.__policy = [[1.0 / n_actions for _ in range(n_actions)] for _ in range(n_states)]
        self.__v = [.0 for _ in range(n_states)]
        self.__q = [[.0 for _ in range(n_actions)] for _ in range(n_states)]

        # Evaluation & Improvement properties
        self.evaluation.set(self.mdp, self.policy, self.v, self.q)
        self.improvement.set(self.mdp, self.policy, self.v, self.q)

    def learn(self, percept):
        """
        Apply the learning method.
        :param percept: percept to learn from.
        :return: the updated policy.
        """
        self.evaluate(percept)
        self.improve()
        return self.policy

    def evaluate(self, percept):
        """
        Update the MDP and apply the evaluation method.
        :param percept: percept to base evaluation on.
        """
        self.mdp.update(percept)
        self.evaluation.evaluate(percept)

    def improve(self):
        """
        Apply the improvement method.
        """
        self.__policy = self.improvement.improve()

    def __str__(self):
        raise NotImplementedError()
