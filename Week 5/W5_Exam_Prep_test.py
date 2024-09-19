
"""
Create a Python function to input item prices and calculate the total amount.

Instructions:
1. Define a Function:
- Name the function `calculate_total_amount`

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
    total_amount = 0.0                                                   # Initialize total amount to 0
    
    print("Enter item prices. Type 'finish' when you are done.")         # Instructions for user
    
    while True:
        user_input = input("Enter price (or type 'finish' to end): ")    # Prompt for item price
        
        if user_input.lower() == "finish":                               # Check for exit condition
            break
        
        try:
            price = float(user_input)                                    # Convert input to float
            if price < 0:                                                # Check for negative price
                print("Price cannot be negative. Please enter a valid price.")  # Error message
                continue                                                 # Skip to next iteration
            total_amount += price                                        # Add valid price to total
        except ValueError:
            print("Invalid input. Please enter a valid number or 'finish' to end.")  # Error message
    
    print(f"Total Amount: ${total_amount:.2f}")                          # Print the total amount

# Example usage:
calculate_total_amount()                                                 # Call the function to calculate total amount
