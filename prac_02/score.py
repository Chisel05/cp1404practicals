"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(get_score_category(score))


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


main()
