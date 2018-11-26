class Percept:
    def __init__(self, cur_state, action, reward, next_state, final):
        self.__s = cur_state
        self.__a = action
        self.__r = reward
        self.__ss = next_state
        self.__final = final

    @property
    def cur_state(self):
        return self.__s

    @property
    def action(self):
        return self.__a

    @property
    def reward(self):
        return self.__r

    @property
    def next_state(self):
        return self.__ss

    @property
    def isfinal(self):
        return self.__final

    def __str__(self):
        return 'current state: ', self.cur_state, '; action: ', self.action, '; reward: ', self.reward, \
               '; next state: ', self.next_state, '; final: ', self.isfinal

    def __repr__(self):
        return self.cur_state, ';', self.action, ';', self.reward, ';', self.next_state, ';', self.isfinal
