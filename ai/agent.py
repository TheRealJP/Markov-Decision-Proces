from random import random


class Agent(object):
    def __init__(self, environment, strategy):
        """ The core for reinforcement learning. The agent "walks" through an environment and tries to learn the
        best possible actions by applying its given learning strategy."""
        self.__environment = environment
        self.__strategy = strategy
        self.__policy = [[.0 for _ in range(self.environment.n_actions)] for _ in range(self.environment.n_states)]

        # Set strategy properties
        self.__strategy.set(environment.n_states, environment.n_actions)

    @property
    def environment(self):
        """Returns the environment the agent is learning."""
        return self.__environment

    @property
    def strategy(self):
        """Returns the learning strategy used by the agent."""
        return self.__strategy

    @property
    def policy(self):
        """Returns the policy used by the agent."""
        return self.__policy

    def learn(self, n_episodes):
        """Plays in the environment for n_episodes
        and improves his policy."""
        for n in range(n_episodes):
            print 'Episode ', n
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
        """Choose the agent's next action through his policy."""
        rnd = random()
        prev = 0
        a = 0

        if self.strategy.improvement.decay >= rnd:
            rnd = random()
            for p in self.policy[s]:
                if p + prev >= rnd:
                    return a
                a += 1
                prev += p

        return int(random() * self.environment.n_actions)

    def __str__(self):
        f = '| {0:>3} | {1:>3} | {2:<4.2} |\n'
        output = f.format('S', 'A', 'Pi') + f.format('=', '=', '=').replace(' ', '=')

        for s in range(len(self.policy)):
            for a in range(len(self.policy[s])):
                output += f.format(s, a, round(self.policy[s][a], 2))
        return output
