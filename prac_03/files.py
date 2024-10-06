# 1.
name = input("Name: ")
file = open('name.txt', 'w')
print(name, file=file)
file.close()

# 2.
file = open('name.txt', 'r')
print(f"Hi {file.read().strip()}!")
file.close()

# 3.
with open('numbers.txt', 'r') as file:
    print(int(file.readline()) + int(file.readline()))

# 4.
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total = total + int(line)
    print(total)
