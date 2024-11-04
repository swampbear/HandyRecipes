class Step:
    def __init__(self, number, description):
        self.number = number
        self.description = description

    def __repr__(self):
        return f"Step({self.number}, {self.description})"

    def __str__(self):
        return f"Step {self.number}: {self.description}"