from ai.environment import Environment


class TurtleBot(Environment):
    def __init__(self):
        self.__n_states = 0
        self.__n_actions = 4
        self.__current_state = 0
        self.__states = [[]]

    @property
    def n_states(self):
        return self.__n_states

    @property
    def n_actions(self):
        return self.__n_actions

    @property
    def current_state(self):
        return self.__current_state

    def reset(self):
        self.__current_state = 0
        return self.current_state

    def step(self, action):
        # TODO
        pass
