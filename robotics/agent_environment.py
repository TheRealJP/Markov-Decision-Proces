import csv
from ai.policy import Policy


class agent_environment:

    def __init__(self):
        self.optimal_path_policy_objects = []
        self.optimal_path = []
        self.current_state = 0
        self.next_state = 0
        self.reward_reached = False
        self.direction_facing = 2  # the robot front is point to this direction

    """
    robot puts a step in the given action/direction
    """

    def step(self, action):
        # todo: stop when reward boolean is true
        # check for limit
        if self.current_state <= len(self.optimal_path_policy_objects) - 1:
            # get the next state & action by moving the robot
            next_state, next_action = self.move_robot(action)

            # update state
            self.current_state = next_state
            # set the action as the current direction of the front of the robot
            self.direction_facing = next_action

            return next_action

    """returns radians"""

    def next_rotation_radians(self, new_direction):
        # assure that there still are next states
        if self.current_state >= len(self.optimal_path_policy_objects) - 1:
            return 0

        pos_rotation = False  # negative rotation
        amount_of_turns = new_direction - self.direction_facing

        # change to positive turn
        if amount_of_turns > 0:
            pos_rotation = True  # positive rotation

        global target_degrees
        abs_aot = abs(amount_of_turns)
        if abs_aot is 1:
            target_degrees = 90 if pos_rotation else -90
        elif abs_aot is 2:
            target_degrees = 180 if pos_rotation else -180
        elif abs_aot is 3:
            target_degrees = 270 if pos_rotation else -270
        else:
            return 0
        return target_degrees  # * math.pi / 180 #todo: uncomment to turn on radians

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
                    self.optimal_path.append([float(row[0]), float(row[1]), float(row[2])])

                    p = Policy(row[0], row[1], row[2])
                    self.optimal_path_policy_objects.append(p)

    """move in the optimal path array"""

    def move_robot(self, direction):
        if self.current_state >= len(self.optimal_path_policy_objects) - 1:
            return 0
