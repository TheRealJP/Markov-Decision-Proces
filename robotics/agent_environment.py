import csv
from ai.policy import Policy


class agent_environment:

    def __init__(self):
        self.optimal_path = []
        self.current_state = 0
        self.next_state = 0
        self.reward_reached = False
        self.direction_facing = 2  # the robot front is point to this direction

    """returns next action in the optimal path"""

    def action_to_take(self, state):
        self.current_state = state

        if self.current_state <= len(self.optimal_path) - 1:  # assure that there still are next states
            return int(self.optimal_path[state].action)

    """returns radians"""

    def next_rotation_radians(self, new_direction):
        global target
        pos_rotation = False
        amount_of_turns = new_direction - self.direction_facing

        # change to positive turn
        if amount_of_turns > 0:
            pos_rotation = True

        abs_aot = abs(amount_of_turns)
        if abs_aot is 1:
            target = 90 if pos_rotation else -90
        elif abs_aot is 2:
            target = 180 if pos_rotation else -180
        elif abs_aot is 3:
            target = 270 if pos_rotation else -270
        else:
            return 0

        return target  # * math.pi / 180 #uncomment to turn on radians

    """
    opencv gives back boolean and tells robot to stop
    if opencv sees the endgoal AND the next action is towards the last state then stop
    """

    def has_reached_reward(self, reward_reached):
        self.reward_reached = reward_reached and self.next_state == len(self.optimal_path) - 1

    """extract the optimal path"""

    def fill_optimal_path(self):
        with open('../voorbeeld_policy.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if float(row[2]) > 0.5:
                    p = Policy(row[0], row[1], row[2])
                    self.optimal_path.append(p)
