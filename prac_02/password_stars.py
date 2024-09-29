"""
Program that prints asterisks the length of a valid, user provided password.
"""


def main():
    minimum_length = 5
    password = get_password()
    while len(password) < minimum_length:
        print(f"Must be >= {minimum_length}!")
        password = get_password()
    print_asterisks(password)


def print_asterisks(string):
    print('*' * len(string))


def get_password():
    password = input("Password: ")
    return password


main()
