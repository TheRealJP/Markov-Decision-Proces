import math

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
from ai.environment import Environment
from ai.percept import Percept
import unittest
import gym
import math


p = []
r = []


# policy overeenkomst
#


# csv file lezen

class TestOpenAI(unittest.TestCase):

    def setUp(self):
        self.env = gym.make('FrozenLake-v0')
        self.env.reset()

    # gegeven dat de huidige actie op state 0 gelijk is aan 1
    # zal de volgende state 0,1 of 4 zijn
    def test_next_state(self):
        actie = 1
        observation, reward, done, info = self.env.step(actie)

        self.assertTrue([0, 1, 4].__contains__(observation))
        self.assertFalse(done)
        self.assertFalse(reward == 1.)
        self.assertTrue(round(info['prob'], 2) == 0.33)

        # print 'actie', actie, \
        #     'volgende state', observation, \
        #     'reward value', reward, \
        #     'klaar?', done, \
        #     'kans', info

    def test_reward_reached(self):
        return

    def test_agent(self):
        assert 1 == 1
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_percept(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_ptsa(self):
        s = 'hello world'


if __name__ == '__main__':
    unittest.main()
