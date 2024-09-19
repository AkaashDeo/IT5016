
"""
Basic Operation of the `elif` Conditional Statement

This program demonstrates the use of the `elif` conditional statement in Python.
It compares two variables, `a` and `b`, and prints a message based on their values.
The `elif` statement allows for additional conditions to be checked if previous conditions were not true.

Author: Akaash Deo

"""

# INPUT
"""Assign values for comparison"""
a = 33
b = 200
# PROCESS & OUTPUT
if b > a:                               # Check if b is greater than a
    print("b is greater than a")

"""Reassign values for another comparison"""
# INPUT
a = 33
b = 33
# PROCESS & OUTPUT
if b > a:                               # Check if b is greater than a; if not, use elif to check if a equals b
    print("b is greater than a")
elif a == b:
    print("a and b are equal")          # If a equals b, print this message

