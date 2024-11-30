"""
Module containing 'SilverServiceTaxi' class.
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class."""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Define SilverServiceTaxi class."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Define string method."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return super().get_fare() + self.flagfall
