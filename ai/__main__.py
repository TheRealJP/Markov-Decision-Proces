from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.monte_carlo import MonteCarlo
from ai.evaluations.n_step_q_learning import NStepQLearning
from ai.evaluations.q_learning import QLearning
from ai.evaluations.value_iteration import ValueIteration
from ai.improvements.with_q import ImprovementWithQ
from ai.improvements.with_v import ImprovementWithV
from ai.policy_writers.cmd_writer import CmdWriter
from ai.policy_writers.csv_writer import CsvWriter
from ai.policy_writers.visual_writer import VisualWriter
from ai.strategy import Strategy


def run():
    precision = .1E-3  # value iteration

    discount = .50
    learning_rate = .50
    decay_rate = 0.01  # verminder rate met deze waarde
    decay = 1.  # past aan
    decay_max = 1.  # beginwaarde
    decay_min = .1  # needs to be on .1

    episodes = 1000

    env = OpenAIGym('FrozenLake-v0')
    evaluation = QLearning(precision, learning_rate)
    improvement = ImprovementWithQ(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount)
    agent = Agent(env, strat)
    agent.learn(episodes)

    CmdWriter.write(agent.policy)
    CsvWriter.write(agent.policy)
    VisualWriter.write(agent.policy)
    # print str.format('%s %s \n%s\n%s %s %s %s \n%s')


if __name__ == '__main__':
    run()
