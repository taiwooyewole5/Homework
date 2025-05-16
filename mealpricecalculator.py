# Meal Price Calculator
# This is my meal price calculator assignment with added creativity. My added creativity was the tip I added as "what percentage I would like to tip"

# Get prices and quantities
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Calculate subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"\nSubtotal: ${subtotal:.2f}")

# Get and compute sales tax
sales_tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

# Calculate total
total_before_tip = subtotal + sales_tax

# Ask for tip percentage
tip_rate = float(input("What percentage would you like to tip? "))
tip = total_before_tip * (tip_rate / 100)

# Compute grand total
total = total_before_tip + tip
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")

# Get payment amount and compute change
payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")