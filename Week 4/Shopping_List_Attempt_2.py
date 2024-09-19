def shopping_list():
    """
    Prompts the user to create a shopping list by entering item names and their prices.
    The user can finish entering items by typing 'done'. The function returns the 
    shopping list and the total price of all items.

    Returns:
        tuple: A tuple containing the shopping list (list of tuples) and total price (float).

    Author: Akaash Deo
    """

    shopping_list = []                                             # Define an empty list to store the shopping list items
    total_price = 0                                                # Initialize total price at 0
    
    while True:                                                    # Loop until user decides to finish
        item = input("Enter the name of the item (or type 'done' to finish): ")  # Prompt for item name
        if item.lower() == 'done':                                 # Check for exit condition
            break                                                  # Exit loop if the user types 'done'
        
        try:
            price = float(input(f"Enter the price of '{item}': ")) # Prompt for item price
            shopping_list.append((item, price))                    # Add the item and price to the list as a tuple
            total_price += price                                   # Add the price to the total price
        except ValueError:                                         # Handle cases where the price input is not valid
            print("Please enter a valid numeric number for the price.")  # Error message for invalid input
    
    return shopping_list, total_price                              # Return the shopping list and total price

def main():
    """
    Main function to execute the shopping list program. It welcomes the user,
    calls the shopping_list function, and displays the items and total price.
    """
    print("Welcome to the shopping list program!")                 # Welcome message
    items, total_price = shopping_list()                           # Call shopping_list and unpack the returned values
    
    if not items:                                                  # Check if no items were added
        print("No items were added")                               # Inform user that the list is empty
    else:
        print("\nShopping List:")                                  # Header for the shopping list
        for item, price in items:                                  # Iterate through each item in the list
            print(f"{item}: ${price:.2f}")                         # Display item name and price formatted to 2 decimal places
        print(f"\nTotal price: ${total_price:.2f}")                # Display total price formatted to 2 decimal places

# Run the main function
if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Execute the main function
