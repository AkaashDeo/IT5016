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
    total_amount = 0.0                         # Initialize the total amount to 0
    
    while True:                                # Start an infinite loop to collect prices
        # Input: Prompt user for item price
        user_input = input("Enter the price of the item (or type 'finish' to stop): ")
        
        if user_input.lower() == 'finish':      # Check if user wants to finish input
            break                               # Exit the loop if 'finish' is entered
        
        try:
            price = float(user_input)           # Convert input to float
            total_amount += price               # Add price to total amount
        except ValueError:                      # Handle invalid input
            print("Invalid input. Please enter a numeric value or 'finish' to stop.")
    
    # Output: Display the total amount
    print(f"Total amount: ${total_amount:.2f}")

calculate_total_amount()                        # Run the function to execute the program

 