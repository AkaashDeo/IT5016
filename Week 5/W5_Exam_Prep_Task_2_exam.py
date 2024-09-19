"""
Lab 2 - Summing Up Prices
Create a Python function to input item prices and calculate the total amount.
Instructions:
1. Define a Function:
   - Name the function `calculate_total_amount`.
2. Input Prices:
   - Prompt the user to enter the price of each item.
   - Continue until the user inputs "finish".
3. Calculate Total Amount:
   - Add each entered price to a running total.
4. Display Total Amount:
   - Print the total amount.

Author: Akaash Deo
"""

def calculate_total_amount():
    total_amount = 0.0                                                                 # Initialize total amount to 0
    
    while True:
        user_input = input("Enter the price of the item (or type 'finish' to end): ")  # Prompt the user to enter the price of an item or "finish" to stop

        if user_input.lower() == "finish":                                             # Check for exit condition
            break
        
        try:
            # Convert the input to a float and add to the total amount
            price = float(user_input)
            if price < 0:                                                              # Validate that the price is not negative
                print("Price cannot be negative. Please enter a valid price.")
                continue
            total_amount += price                                                      # Add valid price to total amount
        except ValueError:
            # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    # Print the total amount
    print(f"Total amount: ${total_amount:.2f}")                                        # Format the total amount to two decimal places

# Example usage:
calculate_total_amount()  # Call the function to execute the price summation
