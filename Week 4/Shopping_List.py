def shopping_list():
    """
    Prompts the user to create a shopping list by entering item names and their prices.
    The user can finish entering items by typing 'done'. The function returns the 
    shopping list and the total price of all items.

    Returns:
        tuple: A tuple containing the shopping list (list of tuples) and total price (float).

        Author: Akaash Deo
    """
    shopping_list = []                                                           # Initialize an empty list to store items
    total_price = 0                                                              # Initialize total price to 0

    while True:                                                                  # Start an infinite loop to allow continuous input
        item = input("Enter the name of the item (or type 'done' to finish): ")  # Prompt user for item name
        if item.lower() == 'done':                                               # Check if the user wants to finish
            break                                                                # Exit the loop if 'done' is entered

        try:
            price = float(input(f"Enter the price of '{item}': "))               # Prompt for item price and convert to float
            shopping_list.append((item, price))                                  # Add the item and price as a tuple to the list
            total_price += price                                                 # Accumulate the total price
        except ValueError:
            print("Please enter a valid numeric number for the price.")          # Handle non-numeric input

    return shopping_list, total_price                                            # Return the list of items and total price

def main():
    """
    Main function to execute the shopping list program. It welcomes the user,
    calls the shopping_list function, and displays the items and total price.
    """
    print("Welcome to the shopping list program!")                               # Welcome message
    items, total_price = shopping_list()                                         # Call shopping_list and unpack the returned values

    if not items:                                                                # Check if no items were added
        print("No items were added")                                             # Inform user that the list is empty
    else:
        print("\nShopping List:")                                                # Print header for shopping list
        for item, price in items:                                                # Iterate through each item in the list
            print(f"{item}, ${price:.2f}")                                       # Print item name and price formatted to 2 decimal places
        print(f"\nTotal Price: ${total_price:.2f}")                              # Print the total price formatted to 2 decimal places

if __name__ == "__main__":                                                       # Ensure the script runs only when executed directly
    main()                                                                       # Execute the main function
