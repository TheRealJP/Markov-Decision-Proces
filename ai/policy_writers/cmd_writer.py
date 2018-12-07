from ai.policy_writer import PolicyWriter


class CmdWriter(PolicyWriter):
    def __init__(self):
        pass

    @staticmethod
    def write(agent):
        print agent
