"""
Score menu program
"""

LOW = 0
HIGH = 100


def main():
    """Provide score menu"""
    score = get_valid_score(LOW, HIGH)
    print_menu_options()
    option = input("> ").upper()
    # option = option.upper()

    while option != "Q":
        if option == "G":
            score = get_valid_score(LOW, HIGH)
        elif option == "P":
            result = determine_result(score)
            print_score_and_result(result, score)
        elif option == "S":
            print_stars(score)
        else:  # Option is unknown
            print(f"Option '{option}' is unknown!")
        print_menu_options()
        option = input("> ").upper()
    print("Goodbye!")


def print_stars(amount):
    """Print given number of stars"""
    print("*" * int(amount))


def print_score_and_result(result, score):
    """Print score and its result"""
    print(f"Your score '{score}' = {result}")


def print_menu_options():
    """Print menu options"""
    print("(G)et a valid score\n"  # Gets a score from user between 0 - 100 inclusive
          "(P)rint result\n"  # Prints result from determine result function
          "(S)how stars\n"  # Prints amount of stars equal to score
          "(Q)uit")  # Quits program


def get_valid_score(low, high):
    """Get valid score between two boundaries"""
    score = float(input("Score: "))
    while score < low or score > high:
        print("Invalid score!")
        score = float(input("Score: "))
    return score


def determine_result(score):
    """Determine result from given score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:  # score < 50
        result = "Bad"
    return result


main()
