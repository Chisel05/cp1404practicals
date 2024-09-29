"""
Calculator that is given a number of items by the user & asks for the individual prices of each item from the user,
then calculating the total price. If the total is equal to or exceeds $100, a 10% discount is applied.

PSEUDOCODE:
get number_of_items
for item in number_of_items
    get item_price
    total_price = total_price + item_price
if total_price >= 100
    total_price = total_price * 0.9
display total_price
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
