from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.value_iteration import ValueIteration
from ai.improvements.with_v import ImprovementWithV
from ai.strategy import Strategy


def run():
    precision = .01
    discount = .9
    learning_rate = .75
    decay_rate = 1. / 25
    decay = 1.
    decay_max = 1.
    decay_min = .01
    episodes = 500

    env = OpenAIGym('FrozenLake-v0')
    evaluation = ValueIteration(precision)
    improvement = ImprovementWithV(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount, learning_rate)
    agent = Agent(env, strat)
    agent.learn(episodes)
    print agent


if __name__ == '__main__':
    run()
