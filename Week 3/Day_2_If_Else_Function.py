"""
The following shows how to use the If/else function.

Author: Akaash Deo
"""

def what_to_wear(temperature):                         # Function to determine what to wear based on temperature.
    if temperature > 25:                               # Check if the temperature is greater than 25.
        print("Wear shorts.")                          # Suggest wearing shorts if hot.
    else:                                              # If temperature is 25 or less,
        print("Not hot today!")                        # Inform that it's not hot.
        print("Wear long pants.")                      # Suggest wearing long pants.
    print("Enjoy yourself.")                           # Print a general message.

def main():                                            # Main function to run the program.
    what_to_wear(20)                                   # Call the function with 20 degrees.
    print()                                            # Print a newline for spacing.
    what_to_wear(30)                                   # Call the function with 30 degrees.

main()                                                 # Execute the main function.
