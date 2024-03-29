from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.q_learning import QLearning
from ai.evaluations.monte_carlo import MonteCarlo
from ai.evaluations.value_iteration import ValueIteration
from ai.improvements.with_q import ImprovementWithQ
from ai.policy_writers.cmd_writer import CmdWriter
from ai.policy_writers.csv_writer import CsvWriter
from ai.policy_writers.visual_writer import VisualWriter
from ai.strategy import Strategy


def run():
    # precision = .1E-9
    # discount = .99
    # learning_rate = .8
    # decay_rate = 0.1E-3
    # decay = 1.
    # decay_max = 1.
    # decay_min = .01
    # episodes = 100

    precision = .1E-10
    discount = .25
    # controls how much q value will be uppdated
    learning_rate = .75  # .8
    decay_rate = 0.1E-4  # 0.1E-5
    decay = 1.
    decay_max = 1.
    decay_min = .01
    episodes = 2000

    # episodes 2000
    # lagere decay rate, lage discount , lagere episodes

    env = OpenAIGym('FrozenLake-v0')
    evaluation = QLearning(precision, learning_rate)
    improvement = ImprovementWithQ(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount)
    agent = Agent(env, strat)
    agent.learn(episodes)

    CmdWriter.write(agent.policy)
    CsvWriter.write(agent.policy)
    VisualWriter.write(agent.policy)


if __name__ == '__main__':
    run()
