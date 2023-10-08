"""
Prac 4, list_exercises.py
"""


def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")

    if username in usernames:
        print("Access granted\n")
        for i in range(5):
            number = int(input("Number: "))
            numbers.append(number)
        print(f"The first number is {numbers[0]}"
              f"\nThe last number is {numbers[-1]}"
              f"\nThe smallest number is {min(numbers)}"
              f"\nThe largest number is {max(numbers)}"
              f"\nThe average of the numbers is {sum(numbers) / len(numbers)}")
    if username not in usernames:
        print("Access denied")


main()
