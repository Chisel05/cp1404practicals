"""
Program for score menu
"""


def main():
    """Score menu"""
    print("(G)et a valid score\n"  # Gets a score from user between 0 - 100 inclusive
          "(P)rint result\n"  # Prints result from determine result function
          "(S)how stars\n"  # Prints amount of stars equal to score
          "(Q)uit")  # Quits program
    option = input("> ")
    option = option.upper()
    score = 0

    while option != "Q":
        if option == "G":
            score = int(input("Score: "))
            while score < 0 or score > 100:
                print("Invalid score!")
                score = float(input("Score: "))
        elif option == "P":
            if score < 0 or score > 100:
                result = "Invalid score"
            elif score >= 90:
                result = "Excellent"
            elif score >= 50:
                result = "Passable"
            else:  # score < 50
                result = "Bad"
            print(f"Your score '{score}' = {result}")
        elif option == "S":
            print("*" * score)
        else:  # Unknown option
            print("Unknown option!")
        print("Menu options")
        option = input("> ")
        option = option.upper()
    print("Goodbye!")


main()
