"""
Program that prints asterisks the length of a valid, user provided password.
"""

minimum_length = 5
password = input("Password: ")
while len(password) < minimum_length:
    print(f"Must be >= {minimum_length}!")
    password = input("Password: ")
print('*' * len(password))
