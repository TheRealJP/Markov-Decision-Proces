import unittest
import gym


# policy overeenkomst
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


if __name__ == '__main__':
    unittest.main()
