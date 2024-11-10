"""
Program that reads all guitar entries from a CSV file and stores them in a list of Guitar objects.
"""
from guitar import Guitar


def main():
    """Function reads CSV file, adding each entry as an object within a list"""
    with open('guitars.csv', 'r') as in_file:
        guitars = []
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], parts[1], float(parts[2])))

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
