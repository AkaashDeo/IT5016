"""
Class Exercise: The formula for working out the final amount when a sum is invested at compound interest is: m = p(1 + i)**n
M is the final amount including the principal.
P is the principal amount.
i is the rate of interest (a whole number indicating the % interest) per year.
n is the number of years invested.
Complete the code which calculates the final amount when $100 is invested for 15 years at 10% interest.
The output prints the principal on one line followed by the final amount on the next line: 

Author: Rajiv Deo
"""

# INPUT
principal_amount = 100
number_of_years = 15
interest_rate = 10 / 100                                                 # Converts percentage to decimal
# PROCESS
final_amount = principal_amount * (1 + interest_rate) ** number_of_years # Calculate the final amount using the compound interest formula
#OUTPUT
print("Principal amount: $", principal_amount)                           # Print the principal amount
print("Final amount: $", final_amount)                                   # Print the final amount after investment

