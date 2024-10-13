"""
List exercises from week 4 practical.
"""


def main():
    numbers = []
    for i in range(1, 6):
        number = int(input("Enter a number: "))
        numbers.append(number)

    print_list_facts(numbers)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter a username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def print_list_facts(numbers):
    print(f"The first number is {numbers[0]}"
          f"\nThe last number is {numbers[-1]}"
          f"\nThe smallest number is {min(numbers)}"
          f"\nThe largest number is {max(numbers)}"
          f"\nThe average of the numbers is {sum(numbers) / len(numbers)}")


main()
