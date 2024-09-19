"""
Calculate the final amount of an investment using compound interest.

This program calculates the final amount of an investment based on the principal amount,
the number of years invested, and the interest rate. It demonstrates the use of the compound 
interest formula and takes user input for personalized calculations.

Author: Akaash Deo
"""

"""(Initialize the principal amount, number of years, and annual interest rate)"""
# INPUT
principal = 100                                           # Initial investment amount
years = 15                                                # Number of years for the investment
rate = 10                                                 # Annual interest rate in percentage
# PROCESS
final_amount = principal * (1 + rate / 100) ** years      # Calculate the final amount using the compound interest formula
# OUTPUT
print("Initial amount:", principal)                       # Output the initial investment.
print("Final amount:", final_amount)                      # Output the calculated final amount

"""(Re-initialize the same variables for further demonstration)"""
# INPUT
principal = 100                                           # Initial investment amount
years = 15                                                # Number of years for the investment
rate = 10                                                 # Annual interest rate in percentage
# PROCESS
final_amount = principal * (1 + rate / 100) ** years      # Calculate the final amount again
# OUTPUT
print("Initial amount is $", principal, sep="")           # Print the initial amount with formatting, Output the initial investment with a dollar sign
print()                                                   # Print a blank line for spacing
print("Final amount $", final_amount)                     # Print the final amount with formatting, Output the calculated final amount with a dollar sign

"""Get user input for a personalized investment calculation"""
# INPUT
principal = int(input("Amount to invest?: "))             # Prompt user for the investment amount
years = int(input("Years term?: "))                       # Prompt user for the investment duration in years
rate = 0.10                                               # Set the interest rate at 10%
# PROCESS
total_yield = principal * (1 + rate) ** years             # Calculate the total yield using compound interest formula
# OUTPUT
                                                          # Output the current interest rate information
print("")                                                 # Print a blank line for spacing
print("Our current interest rates are at a solid 10%, so we're basing your calculations off it.")
print("")                                                 # Print a blank line for spacing
                                                          # Output the personalized investment yield information
print("An investment of $", principal, " will yield you a total of $", total_yield, " in ", years, " years time", sep="")  # Display the investment yield details
print("")                                                 # Print a blank line for spacing
