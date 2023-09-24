"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

bonus_amount = 0
sales_total = float(input("Total sales: $"))

while sales_total >= 0:
    if sales_total < 1000:
        bonus_amount = sales_total * 0.1
    elif sales_total >= 1000:
        bonus_amount = sales_total * 0.15
    print(bonus_amount)
    sales_total = float(input("Total sales: $"))
