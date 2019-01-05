from math import pi

from ai.environment import Environment


class TurtleBot(Environment):
    def __init__(self, moving_strategy, turning_strategy):
        """
        The TurtleBot environment. The agent learns to solve a maze.
        :param moving_strategy: the way the robot moves forward
        :param turning_strategy: the way the robot turns
        """
        self.__n_states = 0
        self.__n_actions = 4
        self.__current_state = 0
        self.__states = [[]]
        self.__facing = 0
        self.__moving_strategy = moving_strategy
        self.__turning_strategy = turning_strategy

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
        """
        Move in a direction relative to starting position.
        0: North
        1: East
        2: South
        3: West
        :param action: action to be performed
        :return: Percept
        """
        # TODO
        # moving forward 1m
        self.__moving_strategy.move_forward(1)

        # turning 90 degrees
        self.__turning_strategy.turn(pi / 2)
        pass
