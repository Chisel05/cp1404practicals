"""
files.py
"""


def main():
    # 1.
    name = input("Name: ")
    with open("name.txt", "w") as out_file:
        print(name, file=out_file)

    # 2.
    with open("name.txt", "r") as in_file:
        print(in_file.readline())

    # 3.
    with open("numbers.txt", "r") as in_file:
        numbers = (in_file.readlines())
        print(int(numbers[0]) + int(numbers[1]))

    # 4.
    numbers_total = 0
    with open("numbers.txt", "r") as in_file:
        for lines in in_file:
            numbers_total += int(lines)
        print(numbers_total)


main()
