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
import unittest


class TestStringMethods(unittest.TestCase):

    def test_policy(self):
        self.assertEqual()
        self.assertEqual('foo'.upper(), 'FOO')

    def test_agent(self):
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
