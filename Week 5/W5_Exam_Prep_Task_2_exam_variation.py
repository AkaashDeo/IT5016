"""
Calculate a total based on various student-related fees or expenses. We'll create a function named 
calculate_total_fees that will prompt the user to input different fees 
(e.g., tuition, lab fees, library fees) until they type "finish". 

The function will then calculate and display the total amount.

Example Scenario

In a university context, students might need to input various fees for different services or departments. 
This function will help to tally those fees.

Author: Akaash Deo
"""

def calculate_total_fees():
    total_fees = 0.0                                       # Initialize total fees to 0
    
    print("Enter each fee amount. Type 'finish' when you are done.")
    
    while True:
        # Prompt the user to enter the fee amount or "finish" to stop
        user_input = input("Enter fee amount (or type 'finish' to end): ")
        
        if user_input.lower() == "finish":
            break
        
        try:
            # Convert the input to a float and add to the total fees
            fee = float(user_input)
            if fee < 0:
                print("Fee cannot be negative. Please enter a valid fee amount.")
                continue
            total_fees += fee
        except ValueError:                                   # Handle invalid input that cannot be converted to a float

            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    print(f"Total fees: ${total_fees:.2f}")                  # Print the total fees


# Example usage:
calculate_total_fees()
