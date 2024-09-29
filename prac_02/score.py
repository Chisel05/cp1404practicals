"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint


def main():
    score = int(input("Enter score: "))
    print(f"Your score of {score} is considered {get_score_category(score)}!")
    print_random_score_result()


def get_score_category(score):
    if score > 100 or score < 0:
        score_category = "Invalid score"
    elif score >= 90:
        score_category = "Excellent"
    elif score >= 50:
        score_category = "Passable"
    else:
        score_category = "Bad"
    return score_category


def print_random_score_result():
    random_score = randint(1, 100)
    get_score_category(random_score)
    print(f"Random score of {random_score} is considered {get_score_category(random_score)}!")


main()
