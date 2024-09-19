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
    total_amount = 0.0                                                     # Initialize total amount to 0.0
    print("Enter item prices. Type 'finish' when you are done.")           # Instruction for the user
    
    while True:                                                            # Start an infinite loop to collect item prices
        # Prompt the user to enter the price of each item
        user_input = input("Enter item price (or type 'finish' to end): ")
        
        if user_input.lower() == "finish":                                 # Check if user wants to stop
            break                                                          # Exit the loop if 'finish' is entered
        
        try:
            # Convert the input to a float and add it to the total amount
            price = float(user_input)                                      # Attempt to convert user input to float
            total_amount += price                                          # Add the valid price to the total amount
        except ValueError:
            # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    # Display the total amount
    print(f"Total amount: ${total_amount:.2f}")                            # Print the total amount formatted to two decimal places

# Call the function to test it
calculate_total_amount()                                                   # Execute the function to collect prices and calculate the total
