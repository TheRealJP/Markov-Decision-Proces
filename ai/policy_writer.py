class PolicyWriter:
    @staticmethod
    def write(policy):
        with open("../voorbeeld_policy.csv", "wb") as csv_file:
            for line in policy:
                csv_file.write(line)
