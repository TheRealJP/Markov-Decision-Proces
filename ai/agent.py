from random import random


class Agent(object):
    def __init__(self, environment, strategy):

        """
        The core for reinforcement learning. The agent "walks" through an environment and tries to learn the
        best possible actions by applying its given learning strategy.
        :param environment: the evinronment the agent has to learn.
        :param strategy: strategy used to learn the environment.
        """

        self.__environment = environment
        self.__strategy = strategy
        self.__policy = [[1. / self.environment.n_actions for _ in range(self.environment.n_actions)]
                         for _ in range(self.environment.n_states)]

        # Set strategy properties
        self.__strategy.set(environment.n_states, environment.n_actions)

    @property
    def environment(self):
        """
        :return: the environment the agent is learning.
        """
        return self.__environment

    @property
    def strategy(self):
        """
        :return: the learning strategy used by the agent.
        """
        return self.__strategy

    @property
    def policy(self):
        """
        :return: the policy used by the agent.
        """
        return self.__policy

    def learn(self, n_episodes):
        """
        Plays in the environment for n_episodes
        and improves his policy.
        :param n_episodes: episodes to run.
        """
        for n in range(n_episodes):
            print('Episode ', n)
            state = self.environment.reset()
            final = False
            while not final:
                action = self.next_action(state)
                percept = self.environment.step(action)

                # improve policy
                self.__policy = self.strategy.learn(percept)
                state = percept.new_state
                final = percept.is_final

    def next_action(self, s):
        """
        Choose the agent's next action through his policy.
        :param s: the current state.
        :return: the chosen action.
        """
        rnd = random()
        prev = 0
        a = 0

        for p in self.policy[s]:
            if p + prev >= rnd:
                return a
            a += 1
            prev += p

        return a - 1
