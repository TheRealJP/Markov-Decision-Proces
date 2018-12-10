class PolicyWriter:
    @staticmethod
    def write(policy):
        with open("../policy.csv", "wb") as csv_file:
            for line in policy:
                csv_file.write(line)
