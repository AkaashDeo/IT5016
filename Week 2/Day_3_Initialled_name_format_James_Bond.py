
"""
This program demonstrates how to manipulate strings to create an initialled name format.

It extracts the first letter of a full name and combines it with the last name, 
resulting in a new format: 'First Letter. Last Name'.

Author: Akaash Deo
"""

# INPUT
full_name = "James Bond"                           # Initialize the string variable 'full_name' with the value "James Bond".
# PROCESS
first_letter = full_name[0]                        # Extract the first letter of the full name.
space_index = full_name.find(" ")                  # Find the index of the space character to separate the first and last names.
last_name = full_name[space_index + 1:]            # Extract the last name using slicing, starting from the character after the space.
initialled_name = first_letter + ". " + last_name  # Combine the first letter with a period and the last name.
# OUTPUT
print(initialled_name)                             # Print the initialled name in the format "J. Bond".
