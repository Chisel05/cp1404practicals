"""
Password stars program
"""

LENGTH_MINIMUM = 10


def main():
    password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print("*" * len(password))


def get_password():
    password = input("Password: ")
    while len(password) < LENGTH_MINIMUM:
        password = input("Password is too short!\n"
                         "Password: ")
    return password


main()
