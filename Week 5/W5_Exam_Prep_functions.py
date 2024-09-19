"""
Exam: Prep: Functions

Author: Akaash Deo
"""

# Print Function

print("Hello World")  # "Hello World" is the argument, print is the function and it's the function name too

# Defining your own functions

# Function Definition:
# - Use 'def' to define a function.
# - Followed by the function name, parentheses for parameters, and a colon.
# - Indent the function body, and use 'return' to exit the function.

# Example Below for 1 value
def multiply_by_three(val):
    """
    Multiplies the given value by three and prints the result.

    Parameters:
        val (int or float): The value to be multiplied.
    """
    total = 3 * val  # Calculate the total by multiplying the input value by 3
    print(total)     # Print the total
    return           # Exit the function

# Call the function with an argument
multiply_by_three(4)  # Outputs: 12

# Example Below for 2 values
def multiply_two_values(value1, value2):
    """
    Multiplies two given values and prints the result.

    Parameters:
        value1 (int or float): The first value.
        value2 (int or float): The second value.
    """
    total = value1 * value2  # Calculate the total by multiplying the two input values
    print(total)              # Print the total
    return                    # Exit the function

# Call the function with two arguments
multiply_two_values(10, 5300202)  # Outputs: 53002020
