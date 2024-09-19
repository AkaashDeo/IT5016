"""
Program that calculates a person's age.

This program prompts the user for their name and year of birth, 
then calculates and displays their age based on the current year.

Author: Akaash Deo
"""

# INPUT
current_year = 2024                                                # Define the current year as 2024.
name = input("What is your name: ")                                # Prompt the user to enter their name.
year_of_birth = int(input("What is your year of birth (YYYY): "))  # Prompt the user to enter their year of birth and convert it to an integer.
# PROCESS
age = current_year - year_of_birth                                 # Calculate the age by subtracting the year of birth from the current year.
# OUTPUT
print(f"Hello {name}, you are now {age} years old. Wow!!!")        # Print a greeting message with the user's name and calculated age.
