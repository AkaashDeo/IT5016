"""
The following function calculates the total number of minutes.
The function is passed two parameters: the hours and the minutes.

Author: Akaash Deo
"""

def number_of_minutes(hours, minutes):              # Define the function 'number_of_minutes' with parameters for hours and minutes.
    total_minutes = hours * 60 + minutes            # Calculate the total minutes by converting hours to minutes and adding the minutes.
    return total_minutes                            # Return the total minutes calculated.

"""Example usage of the function with hardcoded values"""
exercise_total = number_of_minutes(3, 44)           # Calculate total minutes for 3 hours and 44 minutes.
print("1.", exercise_total, "minutes")              # Print the result.
print("2.", number_of_minutes(5, 0), "minutes")     # Calculate and print total minutes for 5 hours and 0 minutes.
print("3.", number_of_minutes(11, 540), "minutes")  # Calculate and print total minutes for 11 hours and 540 minutes.

"""Define a second function 'get_minutes' which performs the same calculation"""
def get_minutes(hours, minutes):                    # Define the function 'get_minutes' with parameters for hours and minutes.
    total = hours * 60 + minutes                    # Calculate total minutes similarly.
    return total                                    # Return the total minutes calculated.

"""Example usage of the 'get_minutes' function with hardcoded values"""
total_minutes = get_minutes(3, 44)                  # Calculate total minutes for 3 hours and 44 minutes.
print("1.", total_minutes, "minutes")               # Print the result.
print("2.", get_minutes(5, 0), "minutes")           # Calculate and print total minutes for 5 hours and 0 minutes.
print("3.", get_minutes(11, 540), "minutes")        # Calculate and print total minutes for 11 hours and 540 minutes.

"""Example for user inputs"""
hours = float(input("Enter hours: "))               # Prompt user for the number of hours and convert input to float.
minutes = float(input("Enter minutes: "))           # Prompt user for the number of minutes and convert input to float.
total_minutes = get_minutes(hours, minutes)         # Call the 'get_minutes' function with user inputs.
print(total_minutes, "minutes")                      # Print the total minutes calculated.
