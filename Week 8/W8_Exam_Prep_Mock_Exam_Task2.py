"""Task 2: `requisition_total` Function

The function collects item names and their corresponding prices in a loop until the user decides to stop. 
It maintains a running total of the prices by updating the `total_sum` variable each time a new item is entered.
The loop continues to prompt the user for additional items until the user responds with something other than 'y'.
Finally, the total sum is printed and returned.

Author: Akaash Deo"""

#Solution:

def requisition_total():
    """Collects item names and prices, calculates the total sum.

    Returns:
        float: The total sum of the item prices.
    """
    total_sum = 0  # Initialize the total sum to 0

    while True:  # Start an infinite loop to collect item details
        item_name = input("Enter item name: ")  # Prompt for item name
        price = float(input("Enter item price: "))  # Prompt for item price and convert to float

        # Update the total sum directly
        total_sum += price  # Add the current item's price to the total sum

        another = input("Add another item? (y/n): ")  # Ask if the user wants to add more items
        if another.lower() != "y":  # Check if the response is not 'y'
            break  # Exit the loop if the user does not want to continue

    print(f"Total: ${total_sum:.2f}")  # Print the total sum formatted to two decimal places
    return total_sum  # Return the total sum of item prices

# Call the function
requisition_total()  # Execute the function to collect items and calculate the total


# Explanation
"""

"""
