"""
Prac 4, quick_picks.py
"""
from random import randint

LOW = 1
HIGH = 45
NUMBERS_IN_ROW = 6


def main():
    previous_number = 0

    quick_pick_number = int(input("How many quick picks? "))

    # TODO: Sort list numbers before printing.
    for i in range(quick_pick_number):
        random_numbers = []
        for j in range(NUMBERS_IN_ROW):
            random_number = randint(LOW, HIGH)
            while random_number == previous_number:
                random_number = randint(LOW, HIGH)
            random_numbers.append(random_number)
            previous_number = random_number
            print(f"{random_numbers[j]:2}", end=" ")
        print()


main()
