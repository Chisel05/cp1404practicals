"""
Program that reads all guitar entries from a CSV file and stores them in a list of Guitar objects.
"""
from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Function reads CSV file, adding each entry as an object within a list, requests additional guitars from the user, and writes guitars list to file"""
    with open(FILENAME, 'r') as in_file:
        guitars = []
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    print_sorted_guitars(guitars)

    print(f"\nAdd guitar, or leave blank to exit!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(guitars[-1].name, "added to guitars!")

        print(f"\nAdd guitar, or leave blank to exit!")
        # Name of next guitar, or leave blank to exit loop
        name = input("Name: ")

    save_guitars(guitars)
    print(f"\n{len(guitars)} guitars saved...")


def save_guitars(guitars):
    """Saves list of guitars to file."""
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def print_sorted_guitars(guitars):
    """Prints sorted list of guitars"""
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
