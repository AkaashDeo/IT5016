

"""
Modulus and Floor Division Operations

This program demonstrates the use of modulus and floor division operations in Python. 
It calculates the remainder of division (modulus) and performs floor division to round down to the nearest whole number.

Author: Akaash Deo
"""

# INPUT
result1 = 25 % 3                                   # Perform modulus operations, Remainder when 25 is divided by 3
result2 = 20 % 34                                  # Perform modulus operations, Remainder when 20 is divided by 34
# PROCESS
result3 = 20 // 3                                  # Perform floor division operations, Floor division of 20 by 3, rounds down to 6
result4 = 5 // 7                                   # Perform floor division operations, Floor division of 5 by 7, rounds down to 0
result5 = (25 // 5) % 5                            # Combined floor division and modulus operation, Floor divide 25 by 5 (results in 5), then find the remainder when divided by 5 (results in 0)
# OUTPUT

print(result1, result2, result3, result4, result5) # Print the results of the calculations
