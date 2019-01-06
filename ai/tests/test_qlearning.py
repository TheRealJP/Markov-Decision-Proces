import unittest
from numpy import amax
from ai.percept import Percept


class TestQLearning(unittest.TestCase):

    # initialises variables needed in the test(s)
    def setUp(self):
        # list of q values
        self.q = [[1.961001767322039, 1.9510152513634005, 1.9451277663886386, 1.9401871789205922],
                  [1.9400902940831364, 1.8835368145869011, 1.8896041395427101, 1.9085586483394537],
                  [1.8763163138927601, 1.7731535392537263, 1.7606468285254999, 1.8181759538406865],
                  [1.7058921159750169, 1.7481135970800807, 1.6922029513739907, 1.7040799531748523],
                  [1.9772445608140841, 1.959120592356917, 1.9553649432255027, 1.9402274889303155],
                  [1.9529698863258487, 1.91847682454204, 1.931055709551784, 1.9201186000966255],
                  [1.8998124630334867, 1.862030274160013, 1.7758196222364582, 1.7852488256527683],
                  [1.8732193184306745, 1.6580622682114285, 1.6600745331419726, 1.6607264394295684],
                  [1.911471054267893, 1.9462171116458986, 1.8938574111776691, 2.0099936100654539],
                  [1.9770249746650834, 2.076219247324969, 1.9248813837189052, 1.9515617720820642],
                  [2.080801024298248, 1.8329753465004828, 1.6979935548684308, 1.4954503991818555],
                  [1.0819248588652961, 1.2303505537191577, 1.3058680686942832, 1.1681985586235362],
                  [1.811251531128947, 1.7307175299176094, 1.7751321071170347, 1.8038776131528378],
                  [1.6813309135877614, 2.1015241943134888, 2.2318807643184457, 2.1463236882053836],
                  [2.2219859519023655, 2.6506153937438395, 2.7478806063227434, 2.9572700106628034],
                  [0.62884366173861617, 0.97256865531221726, 0.79853043013492364, 0.51819880362542359]]

        # list of v values
        self.v = [1.961001767322039, 1.9400902940831364, 1.8763163138927601, 1.7481135970800807, 1.9772445608140841,
                  1.9529698863258487, 1.8998124630334867, 1.8732193184306745, 2.0099936100654539, 2.076219247324969,
                  2.080801024298248, 1.3058680686942832, 1.811251531128947, 2.2318807643184457, 2.9572700106628034,
                  0.97256865531221726]

        # list of rewards
        self.r = [[0., 0., 0., 0.],
                  [0., .0, 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 0., 0., 0.],
                  [0., 1., 0., 1.],
                  [0., 0., 0., 0.]]

        # percept mock (hier mee spelen om andere resultaten te krijgen qua q value)
        self.percept = Percept(prev_state=5, action=0, reward=1, new_state=6, final=False)

        # mdp mock
        self.n_states = 16
        self.n_actions = 4
        self.discount = .25
        self.learning_rate = 0.75

    # this test mocks the evaluate(self,percept) method
    # comparison of old vs new q value given a new percept enters the evaluate(self,percept) method
    def test_evaluate_policy_values(self):
        s = self.percept.prev_state
        a = self.percept.action
        s_ = self.percept.new_state

        old_q_value = self.q[s][a]
        print 'old q value for state ', s, 'and action ', a, ' before incoming percept:', old_q_value
        # Qlearning evaluation
        self.q[s][a] += self.learning_rate * (self.r[s][a] + self.discount *
                                              amax([self.q[s_][a_] - self.q[s][a]
                                                    for a_ in range(self.n_actions)]))
        new_q_value = self.q[s][a]
        print 'new q value for state ', s, 'and action ', a, ' after incoming percept:', new_q_value

        # update v value with highest q value in the current state (prev_state)
        if amax(self.q[s]) not in self.v:
            print 'prev_state to update:', s, \
                '| old v value', self.v[s], \
                '| max q value to replace old v value: ', amax(self.q[s])

        old_v = self.v[s]
        self.v[s] = amax(self.q[s])
        new_v = self.v[s]
        print 'new v value for state', s, ' is: ', new_v

        # actual tests
        self.assertIsNotNone((old_v, new_v, old_q_value, new_q_value))
        self.assertFalse(old_v is new_v)
        self.assertFalse(old_q_value is new_q_value)


if __name__ == '__main__':
    unittest.main()
