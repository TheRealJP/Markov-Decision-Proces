import gym

from ai.environment import Environment
from ai.percept import Percept


class OpenAIGym(Environment):
    def __init__(self, env_name):
        """A wrapper for the OpenAI Gym Environments."""
        self.__env = gym.make(env_name)
        self.__cur_state = self.env.reset()

    @property
    def env(self):
        """Returns the OpenAI Gym Environment."""
        return self.__env

    @property
    def n_states(self):
        return self.env.observation_space.n

    @property
    def n_actions(self):
        return self.env.action_space.n

    @property
    def current_state(self):
        return self.__cur_state

    def reset(self):
        return self.env.reset()

    def step(self, action):
        observation, reward, done, info = self.env.step(action)
        percept = Percept(self.current_state, action, reward, observation, done)
        self.__cur_state = observation
        return percept
