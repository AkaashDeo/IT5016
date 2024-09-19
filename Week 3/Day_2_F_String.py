"""
The following function shows how to use the F string.

Author: Rajiv Deo
"""

name = input("Enter your name: ")                                # Prompt the user for their name.
age = input("Enter your age: ")                                  # Prompt the user for their age.
print("Hello ", name, ". You are ", age, " years old.", sep="")  # Print greeting using traditional string concatenation.

# Using f-string for formatted output
print(f"Hello, {name}, you are {age} years old.")                # Print greeting using f-string for better readability.
