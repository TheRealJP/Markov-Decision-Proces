import csv

from ai.policy import Policy


class AgentEnvironment:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.optimal_path = []
        self.optimal_path_2D = [[None for _ in range(column)] for _ in range(row)]  # replace with incoming parameters
        self.current_state = 0
        self.next_state = 0
        self.reward_reached = False
        self.direction_facing = 2  # the robot front is point to this direction

    """
    robot puts a step in the given action/direction
    change state and face_direction
    """

    def step(self, action):
        # todo: stop when reward boolean is true
        # check for limit
        if self.current_state <= len(self.optimal_path) - 1:
            # get the next state & action by moving the robot
            next_state, next_action = self.move_robot(action)
            self.current_state = next_state  # update state
            self.direction_facing = next_action  # set the action as the current direction of the front of the robot

            return next_action

    """returns radians"""

    def next_rotation_radians(self, new_direction):
        # assure that there still are next states
        if self.current_state >= len(self.optimal_path) - 1:
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
        last_row = 0

        with open('../voorbeeld_policy.csv', 'r') as f:
            reader = csv.reader(f)
            for r in reader:
                if float(r[2]) > 0.5:
                    p = Policy(r[0], r[1], r[2])
                    self.optimal_path.append(p)

            for r in range(self.row):
                for c in range(self.column):
                    self.optimal_path_2D[r].append(self.optimal_path[last_row + c])
            last_row += self.row

    """move in the optimal path array"""

    def move_robot(self, direction):

        if self.current_state >= len(self.optimal_path) - 1:
            return 0, 0

        if direction == 0:  # left
            index = self.current_state - 1
        elif direction == 1:  # down
            index = self.current_state + len(self.optimal_path_2D[0])  # length of row
        elif direction == 2:  # righ
            index = self.current_state + 1
        elif direction == 3:  # up
            index = self.current_state - len(self.optimal_path_2D[0])
        else:
            index = 0

        next_action = self.optimal_path[index].action
        next_state = self.optimal_path[index].state
        return next_action, next_state
