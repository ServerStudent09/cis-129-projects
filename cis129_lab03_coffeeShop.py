# ModuleLab3.py
"""Designing a program to create a coffee shop reciept with muffins, coffees, and a six percent tax rate."""

# Define the Variables
coffee_price = 5.00
muffin_price = 4.00
cappuccino_price = 7.00
latte_price = 7.00
tax_rate = 0.06 #6% tax rate
coffee_number = int(input('Coffees bought: '))
muffin_number = int(input('Muffins bought: '))
cappuccino_number = int(input('Cappuccinos bought: '))
latte_number = int(input('Lattes bought: '))

# Create Functions
subtotal = (coffee_number * coffee_price) + (muffin_number * muffin_price) + (cappuccino_number * cappuccino_price) + (latte_number * latte_price)

tax = subtotal * tax_rate

total = subtotal + tax

# Print Receipt
print("Quick Stop Coffee Shop")

print('Number of Coffees: ' ,coffee_number)

print('Number of Muffins: ' ,muffin_number)

print('Number of Cappuccinos: ' ,cappuccino_number)

print('Number of Lattes: ' ,latte_number)

print(coffee_number, 'Coffee(s) at $5 each: $' ,coffee_number * coffee_price)

print(muffin_number, 'Muffin(s) at $4 each: $' ,muffin_number * muffin_price)

print(cappuccino_number, 'Cappuccino(s) at $7 each: $' ,cappuccino_number * cappuccino_price)

print(latte_number, 'Latte(s) at $7 each: $' ,latte_number * latte_price)

print('6% tax:' ,tax)

print('$' ,total)
