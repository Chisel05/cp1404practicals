numbers = [3, 1, 4, 1, 5, 9, 2]

# Q: numbers[0]
# A: 3

# Q: numbers[-1]
# A: 2

# Q: numbers[3]
# A: 1

# Q: numbers[:-1]
# A: [3, 1, 4, 1, 5, 9]

# Q: numbers[3:4]
# A: [1]

# Q: 5 in numbers
# A: True

# Q: 7 in numbers
# A: False

# Q: "3" in numbers
# A: False

# Q: numbers + [6, 5, 3]
# A: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
