class Percept:
    def __init__(self, prev_state, action, reward, new_state, final):
        """
        The information given by the Environment upon taking an action.
        :param prev_state: the previous state.
        :param action: the taken action.
        :param reward: the given reward.
        :param new_state: the new state.
        :param final: is it a final state?
        """
        self.__s = prev_state
        self.__a = action
        self.__r = reward
        self.__s_ = new_state
        self.__final = final

    @property
    def prev_state(self):
        """
        :return: the state before the action was taken.
        """
        return self.__s

    @property
    def action(self):
        """
        :return: the action that was taken from the previous state.
        """
        return self.__a

    @property
    def reward(self):
        """
        :return: the reward given for taking the action from the previous state.
        """
        return self.__r

    @property
    def new_state(self):
        """
        :return: the new state after taking action.
        """
        return self.__s_

    @property
    def is_final(self):
        """
        :return: true if the action led to a final state, otherwise false.
        """
        return self.__final

    def __str__(self):
        return 'current state: ', self.prev_state, '; action: ', self.action, '; reward: ', self.reward, \
               '; next state: ', self.new_state, '; final: ', self.is_final

    def __repr__(self):
        return self.prev_state, ';', self.action, ';', self.reward, ';', self.new_state, ';', self.is_final
