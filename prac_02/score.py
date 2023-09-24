"""
CP1404/CP5632 - Practical
Program to determine score result
"""

from random import randint


def main():
    """Determine and print score result with a random score result"""
    score = float(input("Enter score: "))
    random_score = randint(0, 100)

    print(f"Your score '{score}' is: {determine_score_result(score)}\n"
          f"Random score '{random_score}' is: {determine_score_result(random_score)}")


def determine_score_result(score):
    """Determine score result from provided value"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:  # score < 50
        return "Bad"


main()
