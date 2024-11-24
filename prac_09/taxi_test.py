"""
Test taxi program from the week 9 practical.
"""
from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)
    # First fare (don't have to start fare because it's already at 0).
    my_taxi.drive(40)
    print(f"{my_taxi}, fare: ${my_taxi.get_fare()}")
    # Second fare.
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, fare: ${my_taxi.get_fare()}")


main()
