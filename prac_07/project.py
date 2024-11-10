"""
Module containing Project class.
"""
from datetime import date


class Project:
    """Class that encapsulates the attributes of a project, with useful project related methods."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create Project class with following attributes."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Represent attributes of self"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Overload less-than operator with priority comparison."""
        return self.priority < other.priority

    def update_project(self, new_percentage, new_priority):
        """Verifies new values as valid & updates self accordingly. If values are invalid, self is assigned its existing values."""
        if 0 <= new_priority <= 100:
            self.priority = new_percentage
        self.completion_percentage = new_percentage
        if 0 < new_priority <= 10:
            self.priority = new_priority

    def get_converted_start_date(self):
        """Converts start date string to Date object from datetime module"""
        day, month, year = self.start_date.split('/')
        return date(int(year), int(month), int(day))
