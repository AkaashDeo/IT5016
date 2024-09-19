"""
Task Description:
Create a Python function that categorizes and provides a recommendation based on the payment status, 
which depends on the total amount. In this task, the categorization will involve not just 
simple high/low classification but also handling edge cases where the payment might be overdue or 
needs urgent attention.

Instructions:

Define a Function:
- Name the function check_payment_status.
Categorize Based on Total Amount and Payment Status:
- Paid: If the total amount is greater than $0 but less than or equal to $100.
- Partially Paid: If the total amount is greater than $100 but less than or equal to $200.
- Overdue: If the total amount exceeds $200.
Generate Recommendations:
- For Paid: Recommend “Thank you for your payment.”
- For Partially Paid: Recommend “Please complete the remaining payment.”
- For Overdue: Recommend “Immediate payment is required to avoid penalties.”
Display Status and Recommendation:
- Print the determined status and the corresponding recommendation.
"""

def check_payment_status(total_amount):
    # Determine the payment status based on the total amount
    if total_amount > 0 and total_amount <= 100:
        status = "Paid"
        recommendation = "Thank you for your payment."
    elif total_amount > 100 and total_amount <= 200:
        status = "Partially Paid"
        recommendation = "Please complete the remaining payment."
    elif total_amount > 200:
        status = "Overdue"
        recommendation = "Immediate payment is required to avoid penalties."
    else:
        status = "No Payment"
        recommendation = "No payment has been recorded. Please make a payment."

    # Print the status and recommendation
    print(f"Payment Status: {status}")
    print(f"Recommendation: {recommendation}")

def calculate_total_fees():
    total_fees = 0.0                                                   # Initialize total fees to 0

    print("Enter each fee amount. Type 'finish' when you are done.")
    
    while True:
        # Prompt the user to enter the fee amount or "finish" to stop
        user_input = input("Enter fee amount (or type 'finish' to end): ")
        
        if user_input.lower() == "finish":                             # Check for exit condition
            break
        
        try:
            # Convert the input to a float and add to the total fees
            fee = float(user_input)  
            if fee < 0:                                                # Validate that the fee is not negative
                print("Fee cannot be negative. Please enter a valid fee amount.")
                continue
            total_fees += fee                                          # Add valid fee to total fees
        except ValueError:
            # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    # Return the total fees
    return total_fees  

# Example usage:
total_amount = calculate_total_fees()                                  # Call the function to calculate total fees
check_payment_status(total_amount)                                     # Determine payment status and provide recommendations
