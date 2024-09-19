"""
This program defines a function to calculate the total number of minutes based on the given hours and minutes.
It demonstrates the function's usage with predefined values as well as user input.

Author: Akaash Deo
"""

def get_minutes(hours, minutes):                    # Define a function that accepts hours and minutes as parameters.
    total = hours * 60 + minutes                    # Calculate the total minutes by converting hours to minutes and adding the remaining minutes.
    return total                                    # Return the total minutes.

# OUTPUT for predefined values
total_minutes = get_minutes(3, 44)                  # Call the function with predefined hours and minutes.
print("1.", total_minutes, "minutes")               # Print the total minutes for the first example.
print("2.", get_minutes(5, 0), "minutes")           # Print the total minutes for the second example.
print("3.", get_minutes(11, 540), "minutes")        # Print the total minutes for the third example.

# Example for user inputs
hours = float(input("Enter hours: "))               # Prompt the user to input hours and convert it to float.
minutes = float(input("Enter minutes: "))           # Prompt the user to input minutes and convert it to float.
total_minutes = get_minutes(hours, minutes)         # Call the function with user input values.
print(total_minutes, "minutes")                     # Print the total minutes calculated from user inputs.
