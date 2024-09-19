"""
Program which formats and prints a name within a border of stars.

This program demonstrates how to create a decorative text display 
by centering a name within a border made of asterisks. The border size 
is dynamically calculated based on the length of the name and a given 
number of extra spaces.

Author: Akaash Deo
"""

# INPUT
name = "Alan Turing"                        # Assign the string "Alan Turing" to the variable 'name'.
extra = 3                                   # Assign the integer 3 to the variable 'extra', which will be used for spacing.
# PROCESS
name_length = len(name)                     # Calculate the length of the string 'name' and store it in 'name_length', For "Alan Turing", this length is 11.                                     
stars_length = name_length + extra * 2      # Calculate the total length for the star border, This is the length of the name plus twice the value of 'extra', Here, 'extra' is 3, so stars_length becomes 11 + 3 * 2 = 17.
# OUTPUT
print("*" * stars_length)                   # Print a row of stars, creating the top border.
print(" " * extra + name + " " * extra)     # Print the name centered with 3 spaces on each side.
print("*" * stars_length)                   # Print another row of stars, creating the bottom border.

# INPUT for a different name
name = "Akaash Deo"                         # Assign the string "Akaash Deo" to the variable 'name'.
extras = 3                                  # Set the extra spaces to 3 for the second name display.
name_length = len(name)                     # Calculate the length of the new 'name' string.

# PROCESS
stars_length = name_length + extras * 2     # Calculate the total length for the star border for the new name.
print("*" * stars_length)                   # Print the top border for the new name.
print(" " * extras + name + " " * extras)   # Print the centered name with spaces.
print("*" * stars_length)                   # Print the bottom border for the new name.
