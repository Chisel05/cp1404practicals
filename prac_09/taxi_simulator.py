"""
Taxi simulator program from practical 9.
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program from practical 9."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    fare_total = 0
    print("Let's drive!")
    print_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                fare_total += current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        else:
            print('Invalid option')
        print(f"Bill to date: ${fare_total:.2f}")
        print_menu()
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${fare_total:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def choose_taxi(taxis):
    """Choose taxi from list of taxis."""
    print("Taxis available:")
    print_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice < 0 or taxi_choice > len(taxis) - 1:
        print("Invalid choice")
        return None
    current_taxi = taxis[taxi_choice]
    return current_taxi


def print_taxis(taxis):
    """Print each taxi from a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def print_menu():
    """Print menu options."""
    print("q)uit, c)hoose taxi, d)rive")


main()
