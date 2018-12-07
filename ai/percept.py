class Percept:
    """The information given by the Environment upon taking an action."""
    def __init__(self, cur_state, action, reward, next_state, final):
        """The information given by the Environment upon taking an action."""
        self.__s = cur_state
        self.__a = action
        self.__r = reward
        self.__s_ = next_state
        self.__final = final

    @property
    def prev_state(self):
        """Returns the state before the action was taken."""
        return self.__s

    @property
    def action(self):
        """Returns the action that was taken from the previous state."""
        return self.__a

    @property
    def reward(self):
        """Returns the reward given for taking the action from the previous state."""
        return self.__r

    @property
    def new_state(self):
        """Returns the new state after taking action."""
        return self.__s_

    @property
    def is_final(self):
        """Returns true if the action led to a final state, otherwise it returns false."""
        return self.__final

    def __str__(self):
        return 'current state: ', self.prev_state, '; action: ', self.action, '; reward: ', self.reward, \
               '; next state: ', self.new_state, '; final: ', self.is_final

    def __repr__(self):
        return self.prev_state, ';', self.action, ';', self.reward, ';', self.new_state, ';', self.is_final
