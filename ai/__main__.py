from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.monte_carlo import MonteCarlo
from ai.evaluations.n_step_q_learning import NStepQLearning
from ai.evaluations.q_learning import QLearning
from ai.evaluations.value_iteration import ValueIteration
from ai.improvements.with_v import ImprovementWithV
from ai.strategy import Strategy


def run():
    precision = .01
    discount = .9
    learning_rate = .75
    decay_rate = 25
    decay = 1.
    decay_max = 1.
    decay_min = .01
    episodes = 500

    env = OpenAIGym('FrozenLake-v0')
    evaluation = MonteCarlo(precision, learning_rate)
    improvement = ImprovementWithV(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount)
    agent = Agent(env, strat)
    agent.learn(episodes)
    print agent


if __name__ == '__main__':
    run()
