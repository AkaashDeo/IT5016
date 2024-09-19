
"""
Program that calculates a person's age based on the current year.

This program prompts the user for their name and year of birth, 
calculates their age using the provided current year, and displays 
a message with their name and age.

Author: Akaash Deo
"""

# INPUT
current_year = int(input("Enter current year: "))                            # Prompt the user to enter the current year and convert it to an integer.
name = input("Enter your name: ")                                            # Prompt the user to enter their name.
birth_year = int(input("Enter your year of birth (YYYY): "))                 # Prompt the user to enter their year of birth and convert it to an integer.
# PROCESS
age = current_year - birth_year                                              # Calculate the age by subtracting the birth year from the current year.
# OUTPUT
print("Hello " + name + ", you are now " + str(age) + " years old. Wow!!!")  # Display a message with the user's name and calculated age.
