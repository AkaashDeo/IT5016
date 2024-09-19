"""
CALCULATOR

Author: Rajiv Deo"""

"""Function to add two numbers"""

def add(num1, num2):
    sum = num1 + num2                          # Calculate the sum
    print("Answer:", sum)                      # Output the sum

"""Function to subtract two numbers"""
def subtract(num1, num2):
    sum = num1 - num2                          # Calculate the difference
    print("Answer:", sum)                      # Output the difference

"""Function to divide two numbers"""
def divide(num1, num2):
    sum = num1 / num2                          # Calculate the quotient
    print("Answer:", sum)                      # Output the quotient

"""Function to multiply two numbers"""
def multiply(num1, num2):
    sum = num1 * num2                          # Calculate the product
    print("Answer:", sum)                      # Output the product

# User input for the first number
num1 = float(input("Enter first number: "))    # Convert input to float
# User input for the second number
num2 = float(input("Enter second number: "))   # Convert input to float
# User input for the desired operation
choice = int(input("What would you like to do with these numbers? Enter the corresponding number.\n1. Add\n2. Subtract\n3. Divide\n4. Multiply\nYour choice: "))

                                               # Conditional statements to execute the selected operation
if choice == 1:
    add(num1, num2)                            # Call add function
elif choice == 2:
    subtract(num1, num2)                       # Call subtract function
elif choice == 3:
    divide(num1, num2)                         # Call divide function
elif choice == 4:
    multiply(num1, num2)                       # Call multiply function
else:
    print("Did not recognize that input.")     # Handle invalid input
