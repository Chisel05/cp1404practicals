for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number = int(input('Enter a number: '))
print("*" * number)
print()

# d.
other_number = int(input('Enter another number: '))
for i in range(0, other_number + 1):
    print("*" * i)