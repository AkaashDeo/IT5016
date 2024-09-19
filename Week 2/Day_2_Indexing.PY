"""
Extract letters from a string and demonstrate indexing.

This program initializes a greeting string, extracts the first and last letters
using indexing, and prints them. It also demonstrates the use of indexing 
to retrieve specific characters from a string.

Author: Akaash Deo
"""
# INPUT
greeting = "Hello World"                # Initialize the greeting string
# PROCESS
first_letter = greeting[2]              # Extract the character at index 2 (the third character)
last_letter = greeting[-1]              # Extract the last character of the string using negative indexing
# OUTPUT
print(first_letter, last_letter)        # Print the first and last letters

"""INDEX returns the position of the element in the specified list or the characters in the string"""
# Example usage of indexing (if needed):
# first_letter = greeting[0]  # This would get the first letter 'H'
