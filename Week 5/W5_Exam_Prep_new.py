def calculate_total_fees():
    """
    Calculate the total fees entered by the user.
    Continues to prompt for fee amounts until the user types 'finish'.

    Author: Akaash Deo
    """

    total_fees = 0.0                                                  # Initialize total fees to 0
    
    print("Enter each fee amount. Type 'finish' when you are done.")
    
    while True:                                                       # Start an infinite loop to collect fees
        # Prompt the user to enter the fee amount or "finish" to stop
        user_input = input("Enter fee amount (or type 'finish' to end): ")
        
        if user_input.lower() == "finish":                            # Check if user wants to stop
            break                                                     # Exit the loop if 'finish' is entered
        
        try:
            # Convert the input to a float and add to the total fees
            fee = float(user_input)                                   # Attempt to convert user input to float
            if fee < 0:                                               # Check if the fee is negative
                print("Fee cannot be negative. Please enter a valid fee amount.")
                continue                                              # Skip to the next iteration if fee is negative
            
            total_fees += fee                                         # Add the valid fee to the total fees
        except ValueError:
            # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    # Return the total fees
    return total_fees                                                 # Return the accumulated total fees

# Example usage:
total_amount = calculate_total_fees()                                 # Call the function to calculate total fees
