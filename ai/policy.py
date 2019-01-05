class Policy():
    def __init__(self, state, action, probability):
        self.state = state
        self.action = action
        self.probability = probability

    def __str__(self):
        return 'current state: ', self.state, \
               'action: ', self.action, \
               'probability: ', self.probability
