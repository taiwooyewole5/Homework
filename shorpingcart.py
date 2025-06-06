# Shopping Cart Program with Quantity Tracking
# Creative Feature: Keep note of quantity of items in the cart and avoids multiple entries of the same item.
# I added track features which are add items, view cart, remove items, compute total price, and quit the program. The program allows users to add items with their prices and quantities, view the current contents of the cart, remove items while adjusting quantities, and compute the total price of all items in the cart.

# Lists to store item names, prices, and quantities
item_names = []
item_prices = []
item_quantities = []

print("Welcome to the Shopping Cart Program!")

# Main loop for the shopping cart program
while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add to your cart? ").strip().capitalize()
        price = float(input(f"What is the price of '{item}'? "))
        
        if item in item_names:
            index = item_names.index(item)
            item_quantities[index] += 1
            print(f"'{item}' quantity increased to {item_quantities[index]}.")
        else:
            item_names.append(item)
            item_prices.append(price)
            item_quantities.append(1)
            print(f"'{item}' has been added to the cart.")

    # View cart option
    elif choice == "2":
        if not item_names:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f} x {item_quantities[i]}")

    # Remove item option
    elif choice == "3":
        if not item_names:
            print("Your cart is empty. Nothing to remove.")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]} - ${item_prices[i]:.2f} x {item_quantities[i]}")
            
            to_remove = int(input("Which item would you like to remove? ")) - 1
            if 0 <= to_remove < len(item_names):
                removed_item = item_names[to_remove]
                if item_quantities[to_remove] > 1:
                    item_quantities[to_remove] -= 1
                    print(f"One unit of '{removed_item}' has been removed (remaining: {item_quantities[to_remove]}).")
                else:
                    item_names.pop(to_remove)
                    item_prices.pop(to_remove)
                    item_quantities.pop(to_remove)
                    print(f"'{removed_item}' has been completely removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")

    # Compute total price option
    elif choice == "4":
        if not item_names:
            print("Your shopping cart is empty.")
        else:
            total = 0
            for i in range(len(item_prices)):
                total += item_prices[i] * item_quantities[i]
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
    # Quit option

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
