"""
Module containing 'Band' class.
"""


class Band:
    """Band class."""

    def __init__(self, name: str = ''):
        """Construct a Band with the given name & an empty musicians list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(f'{musician.name} ({musician.instruments})')
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the Band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string representation of the Band playing."""
        play_strings = []
        for musician in self.musicians:
            play_strings.append(musician.play())
        return '\n'.join(play_strings)
