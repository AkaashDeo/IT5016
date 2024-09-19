def calculate_total_amount():
    """
    Calculate the total amount of item prices entered by the user.
    Continues to prompt for item prices until the user types 'finish'.

    Author: Akaash Deo
    """

    total_amount = 0.0                            # Initialize total amount to 0.0

    while True:                                   # Start an infinite loop to collect prices
        # Prompt the user to enter the price of each item
        user_input = input("Enter the price of the item (or type 'finish' to stop): ")
        
        if user_input.lower() == 'finish':        # Check if user wants to stop
            break                                 # Exit the loop if 'finish' is entered
        
        try:
            # Convert the input to a float and add it to the total amount
            price = float(user_input)             # Attempt to convert user input to float
            total_amount += price                 # Add the price to the total amount
        except ValueError:
            # Handle the case where the input is not a valid number
            print("Invalid input. Please enter a numeric value or 'finish' to stop.")
    
    # Print the total amount
    print(f"Total amount: ${total_amount:.2f}")   # Format the total amount to 2 decimal places

# Call the function to test it
calculate_total_amount()                          # Run the function to start collecting prices
