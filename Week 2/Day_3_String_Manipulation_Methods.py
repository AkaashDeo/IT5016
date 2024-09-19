"""
This program demonstrates various string manipulation methods in Python.

Author: Rajiv Deo
"""

# INPUT
text = 'hello world'                         # A string initialized with "hello world".

# PROCESS
text_upper = text.upper()                    # Convert the string to uppercase.
print(text_upper)                            # Print the uppercase version of the string.

# Re-initialize the string
text = 'hello world'                         # Reset the string for further processing.
text_lower = text.lower()                    # Convert the string to lowercase.
print(text_lower)                            # Print the lowercase version of the string.

# OUTPUT
print("Lower function output is:", text.lower())  # Demonstrate the lower() method directly in the output.

# INPUT
a = 10                                      # Variable a initialized to 10.
b = 20                                      # Variable b initialized to 20.

# OUTPUT
print("Value of a and b are:", a, b)       # Print the values of a and b.

# Demonstrating additional string functions
print("Use of capitalize function:", text.capitalize())  # Use capitalize() to capitalize the first letter of the string.

print(text.title())                          # Use title() to capitalize the first letter of each word in the string.
print(text.swapcase())                       # Use swapcase() to switch the case of each character in the string.

# INPUT
text = 'hello world'                         # Re-initialize the string for further demonstration.
a = text.upper()                            # Convert the string to uppercase.
print(a)                                     # Print the uppercase version of the string again.

# Re-initialize the string
text = 'hello world'                         # Reset the string for additional processing.
a = text.lower()                             # Convert the string to lowercase again.
print(a)                                     # Print the lowercase version of the string again.
