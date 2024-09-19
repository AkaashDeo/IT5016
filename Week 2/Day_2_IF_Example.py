"""
Basic operation of the IF conditional statement.

Author: Akaash Deo

"""

# Example 1

"""In this example we use two variables, a and b, which are used as part of the if statement to test whether b 
is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so 
we print to screen that "b is greater than a"."""
# INPUT
a = 33
b = 200
# PROCESS & OUTPUT
if b > a:
  print("b is greater than a")

#Example 2

"""In this example, we perform basic arithmetic operations based on user input. 
We prompt the user for two numbers and an operator, then use conditional statements to 
determine which operation to perform and print the result."""

# INPUT
firstnum = float(input("Enter your first number: "))           # Prompt the user to enter the first number and convert it to a float
operator = str(input("Enter your operator (*, /, +, -): "))    # Prompt the user to enter the arithmetic operator
secondnum = float(input("Enter your second number: "))         # Prompt the user to enter the second number and convert it to a float
# PROCESS & OUTPUT
if operator == "*":                                            # Check if the operator is multiplication
    result = firstnum * secondnum                              # Calculate the product of the two numbers
    print(result)                                              # Print the result of multiplication

if operator == "/":                                            # Check if the operator is division
    result = firstnum / secondnum                              # Calculate the quotient of the two numbers
    print(result)                                              # Print the result of division

if operator == "+":                                            # Check if the operator is addition
    result = firstnum + secondnum                              # Calculate the sum of the two numbers
    print(result)                                              # Print the result of addition

if operator == "-":                                            # Check if the operator is subtraction
    result = firstnum - secondnum                              # Calculate the difference between the two numbers
    print(result)                                              # Print the result of subtraction

# ONE LINE if statement
if a > b: print("a is greater than b")  # A single line if statement to check if a is greater than b and print the message
