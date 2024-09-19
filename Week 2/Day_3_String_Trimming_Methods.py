"""
This program demonstrates the use of string methods for trimming whitespace and specific characters.

Author: Rajiv Deo
"""

"""Example 1"""
# INPUT
txt = "       python      "                # A string with leading and trailing spaces.
print(len(txt))                            # Print the length of the original string, including spaces.
# PROCESS & OUTPUT
result = txt.strip()                       # Use the strip() method to remove leading and trailing whitespace.
print(result)                              # Print the trimmed string.
print('Length of trimmed version:', len(result))  # Print the length of the trimmed string.

"""Example 2"""
# INPUT
txt = "...trgf.....python...rtgf..."       # A string containing specific characters to trim.
# PROCESS & OUTPUT
r = txt.strip('.rtgf')                     # Use strip() to remove specified characters from both ends of the string.
print(r)                                   # Print the result after trimming specified characters.

r = txt.lstrip('.rtgf')                    # Use lstrip() to remove specified characters from the left side of the string.
print(r)                                   # Print the result after left trimming.

r = txt.rstrip('.rtgf')                    # Use rstrip() to remove specified characters from the right side of the string.
print(r)                                   # Print the result after right trimming.
