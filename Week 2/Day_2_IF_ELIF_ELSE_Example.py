"""
Basic Operation of Conditional Statements: if, elif, and else

This program demonstrates the use of conditional statements in Python: `if`, `elif`, and `else`.
It compares two variables, `a` and `b`, and prints a message based on their values.

Author: Akaash Deo

"""

# INPUT
a = 200                           # Define the variable A
b = 33                            # Define the variable B
# PROCESS & OUTPUT
if b > a:                         # Conditional statements to compare values of `a` and `b`
    print("b is greater than a")  # If b is greater than a, print this message
elif a == b:                      # Conditional statements to compare values of `a` and `b`
    print("a and b are equal")    # If a is equal to b, print this message
else:
    print("a is greater than b")  # If neither of the above conditions are true, this block will execute
