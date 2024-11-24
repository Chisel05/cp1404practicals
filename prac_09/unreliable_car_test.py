"""
Program for testing the 'UnreliableCar' class.
"""
from unreliable_car import UnreliableCar


def main():
    """Program that tests the UnreliableCar class."""
    my_unreliable_car = UnreliableCar("Prius 1", 100, 40)
    my_unreliable_car.drive(40)
    print(f"{my_unreliable_car}")


main()
