"""
Calculate the lengths of strings and demonstrate the use of the len() function.

This program initializes several strings and uses the len() function to determine
the number of characters in each string. It then prints the lengths of the strings.

Author: Akaash Deo
"""

# INPUT
word1 = "Fantastico"       # Initialize the first word
# PROCESS
len1 = len(word1)          # Calculate the length of the first word
len2 = len("012 3 4")      # Calculate the length of another string containing numbers and spaces
# OUTPUT
print(len1, len2)          # Print the lengths of both strings

"""Re-initialize word1 to demonstrate repeated usage (optional)"""

# INPUT
word1 = "Fantastico"  
# PROCESS
len1 = len(word1)          # Calculate the length of the first word again (this is redundant in this context)
len2 = len("012 3 4")      # Calculate the length of the same string containing numbers and spaces again (redundant)
# OUTPUT
print(len1, len2)          # Print the lengths of both strings again (also redundant)

"""Initialize another word"""

# INPUT
word11 = "Blah!"  
# PROCESS
len12 = len(word11)        # Calculate the length of this new word
# OUTPUT
print(len12)               # Print the length of the new word
