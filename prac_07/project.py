"""
Module containing Project class.
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create Project class with following attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def update_project(self, new_percentage, new_priority):
        if 0 <= new_priority <= 100:
            self.priority = new_percentage
        self.completion_percentage = new_percentage
        if 0 < new_priority <= 10:
            self.priority = new_priority
