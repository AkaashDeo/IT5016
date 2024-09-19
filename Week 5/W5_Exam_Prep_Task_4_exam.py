# Lab 4: In this task, you will be required to demonstrate your ability to call other functions and 
# display their results.

"""
Create a function to produce a detailed report based on user data and categorization which
have created in the lab 1 - 4.
Instructions:
1. Define a Function: Name the function `create_detailed_report`.
2. Display Report Information:
• User's Name
• Total Amount
• Category
• Recommendation
3. Format the Output: Ensure the report is well-organized and clear.

Author: Akaash Deo
"""
def collect_user_data(id_counter):
    name = input("Enter your name: ")                                # Prompt for user's name
    age = input("Enter your age: ")                                  # Prompt for user's age
    email = input("Enter your email: ")                              # Prompt for user's email
    
    unique_id = id_counter + 1                                       # Generate unique ID
    id_counter = unique_id                                           # Update counter
    
    return name, unique_id, id_counter                               # Return collected data

def calculate_total_fees():
    total_fees = 0.0                                                 # Initialize total fees to 0
    
    print("Enter each fee amount. Type 'finish' when you are done.")  # Instructions for user
    
    while True:
        user_input = input("Enter fee amount (or type 'finish' to end): ")  # Prompt for fee amount
        
        if user_input.lower() == "finish":                           # Check for exit condition
            break
        
        try:
            fee = float(user_input)                                  # Convert input to float
            if fee < 0:                                              # Check for negative fees
                print("Fee cannot be negative. Please enter a valid fee amount.")  # Error message
                continue                                             # Skip to next iteration
            total_fees += fee                                        # Add valid fee to total
        except ValueError:
            print("Invalid input. Please enter a valid number or 'finish' to end.")  # Error message
    
    return total_fees                                                # Return total fees

def check_payment_status(total_amount):
    if total_amount > 0 and total_amount <= 100:                     # Check if payment is within range
        status = "Paid"                                              # Set status to "Paid"
        recommendation = "Thank you for your payment."               # Recommendation
    elif total_amount > 100 and total_amount <= 200:                 # Check for partially paid
        status = "Partially Paid"                                    # Set status to "Partially Paid"
        recommendation = "Please complete the remaining payment."    # Recommendation
    elif total_amount > 200:                                         # Check for overdue
        status = "Overdue"                                           # Set status to "Overdue"
        recommendation = "Immediate payment is required to avoid penalties."  # Recommendation
    else:
        status = "No Payment"                                        # Handle no payment case
        recommendation = "No payment has been recorded. Please make a payment."  # Recommendation
    
    return status, recommendation                                    # Return status and recommendation

def create_detailed_report(id_counter):
    # Collect user data
    name, unique_id, updated_counter = collect_user_data(id_counter)  # Gather user info
    
    # Calculate total fees
    total_amount = calculate_total_fees()                             # Get total fees from user
    
    # Check payment status
    status, recommendation = check_payment_status(total_amount)        # Determine payment status
    
    # Generate the detailed report
    print("\n--- Detailed Report ---")                                 # Header
    print(f"User Name: {name}")                                        # Print user name
    print(f"Unique ID: {unique_id}")                                   # Print unique ID
    print(f"Total Amount: ${total_amount:.2f}")                        # Print total amount
    print(f"Category: {status}")                                       # Print payment status
    print(f"Recommendation: {recommendation}")                         # Print recommendation
    print("------------------------\n")                                # Footer
    
    # Return updated counter if needed for further use
    return updated_counter                                             # Return updated ID counter

# Example usage:
current_counter = 5000  # Initialize the current counter
current_counter = create_detailed_report(current_counter)  # Generate report
