"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Temperature conversion program from Celsius to Fahrenheit, and vice versa"""
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def print_menu():
    print("C - Convert Celsius to Fahrenheit\n"
          "F - Convert Fahrenheit to Celsius\n"
          "Q - Quit")


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
