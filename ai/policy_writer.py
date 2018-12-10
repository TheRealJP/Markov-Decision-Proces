class PolicyWriter:
    @staticmethod
    def write(policy):
        with open("../policy.csv", "w") as csv_file:
            for line in policy:
                csv_file.write(line)
