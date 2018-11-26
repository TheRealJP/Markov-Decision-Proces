class Evaluation(object):
    def __init__(self, precision):
        self.__mdp = None
        self.__policy = None
        self.__v = None
        self.__q = None
        self.__precision = precision

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
    def precision(self):
        return self.__precision

    def set(self, mdp, policy, v, q):
        self.__mdp = mdp
        self.__policy = policy
        self.__v = v
        self.__q = q

    def evaluate(self, percept):
        raise NotImplementedError()
