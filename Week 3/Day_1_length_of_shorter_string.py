"""
This program defines a function that takes two strings as input and returns the length of the shorter string.

Author: Rajiv Deo
"""

def function2(word1, word2):                       # Define a function that accepts two string parameters: word1 and word2.
    len1 = len(word1)                              # Calculate the length of the first string.
    len2 = len(word2)                              # Calculate the length of the second string.
    shorter_length = min(len1, len2)               # Find the minimum length between the two strings.
    return shorter_length                          # Return the length of the shorter string.

# INPUT
word1 = input("Enter word 1: ")                    # Prompt the user to input the first string.
word2 = input("Enter word 2: ")                    # Prompt the user to input the second string.
# OUTPUT
print(function2(word1, word2))                     # Call the function with the input strings and print the result.
