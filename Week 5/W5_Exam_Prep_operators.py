"""
Arithmetic operators (do maths).

Author: Akaash Deo
"""

"""Modulus operator: gives the remainder of the division"""
remainder = 20 % 6
print(f"20 % 6 = {remainder}")                         # Output the result of modulus operation

"""Arithmetic Operators with Strings"""

"""Concatenation of two strings"""
x = "string1" + "string2"
print(f"Concatenated string: {x}")                     # Output the concatenated string

"""Repetition of a string"""
x = "string1" * 10
print(f"Repeated string: {x}")                         # Output the repeated string

"""Comparison, Logical, and Membership Operators"""

"""Comparison Operators"""

x = True == True                                       # Checks if True is equal to True
print(f"True == True: {x}")

x = True != True                                       # Checks if True is not equal to True
print(f"True != True: {x}")

x = 5 < 1                                              # Checks if 5 is less than 1
print(f"5 < 1: {x}")

"""Logical Operators: operate on boolean values"""

x = True and True                                      # Both operands are True
print(f"True and True: {x}")

x = True and False                                     # One operand is False
print(f"True and False: {x}")

x = True or False                                      # At least one operand is True
print(f"True or False: {x}")

x = "yiii" or "z"                                      # Returns the first truthy value
print(f"'yiii' or 'z': {x}")

# Negation using 'not'
print(f"not True: {not True}")                         # Output: False
print(f"not False: {not False}")                       # Output: True

# Membership Operators: 'in', 'not in'

is_in_list = 1 in [1, 2, 3, 4, 5]                      # Checks if 1 is in the list
print(f"Is 1 in [1, 2, 3, 4, 5]? {is_in_list}")        # Output the result
