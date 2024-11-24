"""
Program for testing the 'SilverServiceTaxi' class.
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Program that tests the SilverServiceTaxi class."""
    my_silver_service_taxi = SilverServiceTaxi(name='Hummer', fanciness=2, fuel=200)
    my_silver_service_taxi.drive(18)
    assert my_silver_service_taxi.get_fare() == 48.78
    print(my_silver_service_taxi.get_fare())


main()
