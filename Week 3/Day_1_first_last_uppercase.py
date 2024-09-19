"""
This program defines a function that takes a word as input and returns the combination of its first and last letters in uppercase.

Author: Akaash Deo
"""

def function3(word):                               # Define a function that accepts one string parameter: word.
    first = word[0]                                # Extract the first character of the word.
    last = word[len(word) - 1]                     # Extract the last character of the word.
    combined = last + first                        # Concatenate the last and first characters.
    return combined.upper()                        # Return the combined characters in uppercase.

# INPUT
word = input("Enter a Word: ")                     # Prompt the user to input a word.
# OUTPUT
print(function3(word))                             # Call the function with the input word and print the result.
