from random import random


class Agent(object):
    def __init__(self, environment, strategy):
        self.__environment = environment
        self.__strategy = strategy
        self.__policy = [[.0 for _ in range(self.environment.n_actions)] for _ in range(self.environment.n_states)]

        # Set strategy properties
        self.__strategy.set(environment.n_states, environment.n_actions)

    @property
    def environment(self):
        return self.__environment

    @property
    def strategy(self):
        return self.__strategy

    @property
    def policy(self):
        return self.__policy

    def learn(self, n_episodes):
        for n in range(n_episodes):
            print 'Episode ', n
            state = self.environment.reset()
            final = False
            while not final:
                action = self.next_action(state)
                percept = self.environment.step(action)
                # improve policy
                self.__policy = self.strategy.learn(percept)
                state = percept.next_state
                final = percept.isfinal

    def next_action(self, s):
        action = 0
        chance = 0
        rnd = random()

        for p in self.policy[s]:
            if p < chance + rnd:
                return action
            action += 1
            chance += p
        return action

    def __str__(self):
        f = '| {0:>3} | {1:>3} | {2:<4.2} |\n'
        output = f.format('S', 'A', 'Pi') + f.format('=', '=', '=').replace(' ', '=')

        for s in range(len(self.policy)):
            for a in range(len(self.policy[s])):
                output += f.format(s, a, round(self.policy[s][a], 2))
        return output
