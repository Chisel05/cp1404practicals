"""
Module containing 'UnreliableCar' class.
"""
from car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0, 100) <= self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
