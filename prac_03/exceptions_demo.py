"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a valid number is not given to either the numerator or the denominator.
2. When will a ZeroDivisionError occur?
When a zero is given for the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Continue asking for the denominator until a number other than 0 is given.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
