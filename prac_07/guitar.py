"""
Class module containing guitar class.
"""


class Guitar:
    """Represents a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initializes guitar attributes"""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self, year=2024):
        """Gets age of guitar according to given year, or default year if no year is provided"""
        return year - self.year

    def is_vintage(self):
        """Determines if the guitar is considered vintage according to the guitar's age"""
        if self.get_age() >= 50:
            return True
        return False
