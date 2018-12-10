from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.q_learning import QLearning
from ai.improvements.with_v import ImprovementWithV
from ai.policy_writers.cmd_writer import CmdWriter
from ai.strategy import Strategy
from ai.policy_writer import PolicyWriter

def run():
    precision = .1E-9
    discount = .6
    learning_rate = .75
    decay_rate = .1
    decay = 1.
    decay_max = 1.
    decay_min = .01
    episodes = 500

    env = OpenAIGym('FrozenLake-v0')
    evaluation = QLearning(precision, learning_rate)
    improvement = ImprovementWithV(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount)
    agent = Agent(env, strat)
    agent.learn(episodes)
    CmdWriter.write(agent)
    PolicyWriter.write(repr(agent))


if __name__ == '__main__':
    run()
