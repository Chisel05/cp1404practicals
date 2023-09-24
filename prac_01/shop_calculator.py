total_items_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))


for i in range(number_of_items):
    item_price = float(input(f"Price of item: "))
    total_items_price = total_items_price + item_price
print(f"${total_items_price:.2f}")
