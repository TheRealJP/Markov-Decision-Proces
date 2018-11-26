class Environment(object):
    @property
    def n_states(self):
        raise NotImplementedError()

    @property
    def n_actions(self):
        raise NotImplementedError()

    @property
    def current_state(self):
        raise NotImplementedError()

    def reset(self):
        raise NotImplementedError()

    def step(self, action):
        raise NotImplementedError()
