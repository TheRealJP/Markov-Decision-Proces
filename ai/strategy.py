from ai.mdp import MDP


class Strategy(object):
    def __init__(self, evaluation, improvement, discount):
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__evaluation = evaluation
        self.__improvement = improvement
        self.__discount = discount

    @property
    def mdp(self):
        return self.__mdp

    @property
    def policy(self):
        return self.__policy

    @property
    def v(self):
        return self.__v

    @property
    def q(self):
        return self.__q

    @property
    def evaluation(self):
        return self.__evaluation

    @property
    def improvement(self):
        return self.__improvement

    @property
    def discount(self):
        return self.__discount

    def set(self, n_states, n_actions):
        self.__mdp = MDP(n_states, n_actions, self.discount)
        self.__policy = [[1.0 / n_actions for _ in range(n_actions)] for _ in range(n_states)]
        self.__v = [.0 for _ in range(n_states)]
        self.__q = [[.0 for _ in range(n_actions)] for _ in range(n_states)]

        # Evaluation & Improvement properties
        self.evaluation.set(self.mdp, self.policy, self.v, self.q)
        self.improvement.set(self.mdp, self.policy, self.v, self.q)

    def learn(self, percept):
        self.evaluate(percept)
        self.improve()
        return self.policy

    def evaluate(self, percept):
        self.mdp.update(percept)
        self.evaluation.evaluate(percept)

    def improve(self):
        self.__policy = self.improvement.improve()

    def __str__(self):
        raise NotImplementedError()
