
"""
The code calculates the final amount of an investment using compound interest and prints both the initial and final 
amounts. 

It demonstrates how to use newline characters to format output and shows the correct usage of variables 
in a print statement. 

Additionally, it illustrates how to print multiple values on a single line with a default 
space separator and how to customize the separator.

Author: Rajiv Akaash Deo
"""

# INPUT
principal = 100
years = 15
rate = 10
# PROCESS
final_amount = principal * (1 + rate / 100) ** years                                   # Calculate the final amount using compound interest formula
# OUTPUT
print("Initial amount")                                                                # Print the initial amount
print(principal)                                        
print("Final amount")                                                                  # Print the final amount
print(final_amount)
print("Auckland\nWellington")                                                          # Demonstrate the use of newline characters in strings
print("Initial Amount Invested:\n", principal, "\nFinal Amount:\n", final_amount)      # Correct usage of variables in a print statement
print(1, "Whitecliffe", "Manukau")                                                     # Print multiple values on a single line with default space separator
print(1, "Whitecliffe", "Manukau", sep="")                                             # Print multiple values on a single line with no space separator

