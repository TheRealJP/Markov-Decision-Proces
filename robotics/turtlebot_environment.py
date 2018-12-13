from ai.environment import Environment


class TurtleBot(Environment):
    def __init__(self):
        """The TurtleBot environment. The agent learns to solve a maze."""
        self.__n_states = 0
        self.__n_actions = 4
        self.__current_state = 0
        self.__states = [[]]
        self.__facing = 0

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

    def move_forward(self, meters):
        """Make the TurtleBot move forward a set distance."""
        # TODO
        pass

    def turn(self, radians):
        """Make the TurtleBot turn a set amount of radians."""
        # TODO
        pass
