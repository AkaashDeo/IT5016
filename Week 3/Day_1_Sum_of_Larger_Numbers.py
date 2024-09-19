"""
This program defines a function that takes three whole numbers as input and returns the total of the two larger numbers.

Author: Rajiv Deo
"""

def function1(n1, n2, n3):                        # Define a function that accepts three parameters: n1, n2, n3.
    sum = n1 + n2 + n3                            # Calculate the sum of the three numbers.
    minimum = min(n1, n2, n3)                     # Find the minimum of the three numbers.
    return sum - minimum                          # Return the sum minus the minimum value, which gives the total of the two larger numbers.

# INPUT
n1 = int(input("Number 1: "))                     # Prompt the user to input the first number.
n2 = int(input("Number 2: "))                     # Prompt the user to input the second number.
n3 = int(input("Number 3: "))                     # Prompt the user to input the third number.
# OUTPUT
print(function1(n1, n2, n3))                      # Call the function with the input values and print the result.
