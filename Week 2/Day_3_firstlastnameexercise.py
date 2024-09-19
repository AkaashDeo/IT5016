"""
This program demonstrates string multiplication and a function to convert time from hours and minutes to total minutes.

It shows how to create repeated strings and how to define and use a function to calculate total minutes based on user input.

Author: Akaash Deo
"""

# INPUT
praise = "good!"                           # Initialize the string variable 'praise' with the value "good!"
# PROCESS
lot_of_praise = praise * 4                 # Repeat the 'praise' string 4 times and store it in 'lot_of_praise'
# OUTPUT
print(praise)                              # Print the single instance of 'praise'
print(lot_of_praise)                       # Print the repeated string 'lot_of_praise'

"""Re-initialize 'praise' with the same value 'good!'"""
# INPUT
praise = "good!"                           # Re-initialize 'praise' with the value "good!"
# PROCESS
lot_of_praise = praise * 4                 # Repeat the 'praise' string 4 times again and store it in 'lot_of_praise'
# OUTPUT
print(praise)                              # Print the single instance of 'praise' again
print(lot_of_praise)                       # Print the repeated string 'lot_of_praise' again

"""Define a function to convert hours and minutes to total minutes"""
def get_minutes(hours, minutes):           # Function to calculate total minutes from hours and minutes
    total = hours * 60 + minutes           # Calculate total minutes by converting hours to minutes and adding the remaining minutes
    return total                           # Return the total minutes

# INPUT
hours = float(input("Enter hours:"))       # Prompt user for the number of hours and convert input to float
minutes = float(input("Enter minutes:"))   # Prompt user for the number of minutes and convert input to float
# PROCESS
total_minutes = get_minutes(hours, minutes) # Call the function and store the result in 'total_minutes'
# OUTPUT
print(total_minutes, "minutes")            # Print the total minutes calculated

# Example calls to the function with hardcoded values
total_minutes = get_minutes(3, 44)         # Calculate total minutes for 3 hours and 44 minutes
print(get_minutes(5, 0), "minutes")        # Calculate total minutes for 5 hours and 0 minutes
print(get_minutes(11, 540), "minutes")     # Calculate total minutes for 11 hours and 540 minutes
