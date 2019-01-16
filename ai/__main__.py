from ai.agent import Agent
from ai.environments.openai import OpenAIGym
from ai.evaluations.q_learning import QLearning
from ai.improvements.with_q import ImprovementWithQ
from ai.policy_writers.cmd_writer import CmdWriter
from ai.policy_writers.csv_writer import CsvWriter
from ai.policy_writers.visual_writer import VisualWriter
from ai.strategy import Strategy


def run():
    # S F F F <- wilt links boven blijven door 0 || 3
    # F H F H
    # F F F H <- wilt naar onder en rechts door 1 || 2
    # F H F G
    #     discount = .99 ,     learning_rate = .8 ,     decay_rate = 0.0001 ,     episodes = 8000 | 1 goede policy
    #     discount = .6 ,     learning_rate = .75 ,     decay_rate = 0.00001 ,     episodes = 1500 | 5 +/-goede policies

    # alleen gebruikt in value iteration evaluatie
    precision = .1E-10

    # controleert value van toekomstige waarde
    # discount 0 "i only care about immediate rewards", bigger discount farther rewards
    # succesvolle waarden liggen tussen 0.9 - 0.99
    discount = .6

    # controls how much q value will be uppdated
    # niet te groot gaat constant oscileren rond het minimum
    # te klein , te veel stappen nodig
    # moet convergen in het mimimum punt
    learning_rate = .8

    # zorgt voor exploration/exploitation, meer episodes --> lagere decay waarde --> meer exploitation
    # zorgt ervoor dat er meer en meer de juiste actie wordt gekozen (1 - decay wordt opgeteld bij policy(s,a))
    # helpt bij het afbouwen van fluctuaties in het aanpassen van de policy
    # grotere decay rate meer 0
    # te laag --> te weinig onderscheiding tss policy values
    # te hoog -->  meer resources nodig om te berekenen, weinig value...
    decay_rate = 0.0001
    decay = 1.
    decay_max = 1.
    decay_min = .01
    # lambda/decay_rate = 0.1E-3 of 0.1E-4  blijkt ideaal

    # aantal keer leren
    # meer verfijnde policy..
    # oververzadigd na een tijdje
    episodes = 3500

    env = OpenAIGym('FrozenLake-v0')
    evaluation = QLearning(precision, learning_rate)

    # Improves policy
    improvement = ImprovementWithQ(decay_rate, decay, decay_max, decay_min)
    strat = Strategy(evaluation, improvement, discount)
    agent = Agent(env, strat)

    # updates the policy each episode by evaluating percept and improving the policy values
    agent.learn(episodes)

    CmdWriter.write(agent.policy)
    CsvWriter.write(agent.policy)
    VisualWriter.write(agent.policy)

    # reward val: immediate value
    # utility val: long term value


if __name__ == '__main__':
    run()
