"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print(f"Please enter a valid password"
          f"\nYour password must be between {MIN_LENGTH} and {MAX_LENGTH}, and contain:"
          f"\n\t1 or more uppercase characters"
          f"\n\t1 or more lowercase characters"
          f"\n\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    password_length = len(password)
    if password_length < MIN_LENGTH or password_length > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        for special_character in SPECIAL_CHARACTERS:
            if special_character == char:
                count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False
    return True  # password must be valid for True


main()
