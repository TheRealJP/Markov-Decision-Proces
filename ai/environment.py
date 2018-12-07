class Environment(object):
    """The Environment the Agent explores."""
    @property
    def n_states(self):
        """The amount of states in the environment."""
        raise NotImplementedError()

    @property
    def n_actions(self):
        """The amount of actions you can perform."""
        raise NotImplementedError()

    @property
    def current_state(self):
        """The state the environment is currently positioned in."""
        raise NotImplementedError()

    def reset(self):
        """Reset the environment to its initial state."""
        raise NotImplementedError()

    def step(self, action):
        """Take a given action in the environment starting from the current state."""
        raise NotImplementedError()
