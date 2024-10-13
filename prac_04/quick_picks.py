"""
"Quick Pick" Lottery Ticket Generator program from week 4 practical.
"""
from random import randint

LOW = 1
HIGH = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_pick_sets = []
    for number_of_quick_picks in range(1, number_of_quick_picks + 1):
        quick_picks = []
        for i in range(6):
            random_number = randint(LOW, HIGH)
            while random_number in quick_pick_sets:
                random_number = randint(LOW, HIGH)
            quick_picks.append(random_number)
        quick_picks.sort()
        quick_pick_sets.append(quick_picks)

    for quick_picks in quick_pick_sets:
        for pick in quick_picks:
            print(f"{pick:2}", end=" ")
        print()


main()
