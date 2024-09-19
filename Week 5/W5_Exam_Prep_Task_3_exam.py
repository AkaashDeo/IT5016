"""
Task 3: In this task, you will be provided with statements containing various conditions. 
Your objective will be to write Python functions that use control structures to implement the 
provided conditions based on input from another function.

Lab 3 - Decision Based on Total
Create a Python function to categorize and provide a recommendation based on the total
amount which you have done in Lab 2.

Instructions:
1. Define a Function:
   - Name the function `categorize_request`
2. Categorize Based on Total:
   - If the total amount is less than $150, set the category to "Low".
   - If the total amount is $150 or more, assign the category to "High".
3. Generate Recommendation:
   - Based on the category:
     • Low: Recommend “Proceed with standard processing.”
     • High: Recommend “Review for potential discounts.”
4. Display Category and Recommendation:
   - Print the determined category and the corresponding recommendation.

Author: Akaash Deo
"""

def categorize_request(total_amount):
    # Determine the category based on the total amount
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."
    
                                                                                 # Print the category and recommendation
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

def calculate_total_fees():
                                                                                 # Initialize total fees to 0
    total_fees = 0.0  
    
    print("Enter each fee amount. Type 'finish' when you are done.")
    
    while True:
        user_input = input("Enter fee amount (or type 'finish' to end): ")       # Prompt the user to enter the fee amount or "finish" to stop

        
        if user_input.lower() == "finish":                                       # Check for exit condition
            break
        
        try:
            # Convert the input to a float and add to the total fees
            fee = float(user_input)  
            if fee < 0:                                                           # Validate that the fee is not negative
                print("Fee cannot be negative. Please enter a valid fee amount.")
                continue
            total_fees += fee                                                     # Add valid fee to total fees
        except ValueError:                                                        # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    return total_fees                                                             # Return the total fees


# Example:
total_amount = calculate_total_fees()                                             # Call the function to calculate total fees
categorize_request(total_amount)                                                  # Determine payment status and provide recommendations

