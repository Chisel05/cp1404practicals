"""
Score menu program that allows user to provide a score, print the category of their score,
and print a number of asterisks equal to their score.
"""

MENU = ("(G)et valid score (0 - 100)"
        "\n(P)rint result"
        "\n(S)how stars"
        "\n(Q)uit")


def main():
    """Main function containing menu loop."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_category(score))
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Return valid score between 0 and 100."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score! Must be between 0 and 100.")
        score = int(input("Score: "))
    return score


def get_score_category(score):
    """Return category of given score."""
    if score > 100 or score < 0:
        score_category = "Invalid score"
    elif score >= 90:
        score_category = "Excellent"
    elif score >= 50:
        score_category = "Passable"
    else:
        score_category = "Bad"
    return score_category


def print_asterisks(length):
    """Print number of asterisks equal to length variable."""
    print('*' * length)


main()
