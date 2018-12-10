import numpy as np
import csv

from ai.policy import Policy


class agent_environment:
    def __init__(self):
        self.policy = []
        self.current_state = 0
        self.reward_reached = False
        # double array aanmaken
        self.static_map = np.array([[.0 for _ in range(4)] for _ in range(4)])
        # map vullen met xy "coordinaten/posities"

    """
    loop trough policy iteration 
    get next state => "choose_next_state(self)"
    let it execute => "action_to_take(self)"
    signal that you have arrived (something like stopped its ticks)
    if color is different then its a reward
    """

    def action_to_take(self):
        return NotImplementedError

    def reached_reward(self, ):
        self.reward_reached = True

        """"""

    def choose_next_state(self):
        self.next_state = self.current_state

    def __translate_location_to_2D(self):
        return 0

    def __translate_location_to_1D(self):
        return 0

    def fill_policy(self):
        with open('../policy.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                p = Policy(row[0], row[1], row[2])
                self.policy.append(p)
