# ModuleLab3.py
"""Designing a program to create a coffee shop reciept with muffins, coffees, and a six percent tax rate."""

# Define the Variables
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06 #6% tax rate
coffee_number = int(input('Coffees bought: '))
muffin_number = int(input('Muffins bought: '))

# Create Functions
subtotal = (coffee_number * coffee_price) + (muffin_number * muffin_price)

tax = subtotal * tax_rate

total = subtotal + tax

# Print Receipt
print("Quick Stop Coffee Shop")

print('Number of Coffees: ' ,coffee_number)

print('Number of Muffins: ' ,muffin_number)

print(coffee_number, 'Coffee(s) at $5 each: $' ,coffee_number * coffee_price)

print(muffin_number, 'Muffin(s) at $4 each: $' ,muffin_number * muffin_price)

print('6% tax:' ,tax)

print('$' ,total)
