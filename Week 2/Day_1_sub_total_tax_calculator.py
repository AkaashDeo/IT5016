"""
The code prompts the user to input the amounts of three separate purchases, calculates the total subtotal by summing
these amounts, and then computes the tax and grand total. It adds a 15% tax to the subtotal to find the grand total. 
Finally, it prints the grand total amount.

Author: Akaash Deo
"""

# INPUT
purchase1 = float(input("How much was your first purchase?"))       # Prompt user for the amount of the first purchase and convert it to a float
purchase2 = float(input("How much was your second purchase?"))      # Prompt user for the amount of the second purchase and convert it to a float
purchase3 = float(input("How much was your third purchase"))        # Prompt user for the amount of the third purchase and convert it to a float
# PROCESS
total_sub = purchase1 + purchase2 + purchase3                       # Calculate the total subtotal by summing the amounts of all three purchases
tax_sale = total_sub * 0.15                                         # Calculate the sales tax as 15% of the subtotal
grand_total = total_sub + tax_sale                                  # Calculate the grand total by adding the subtotal and the sales tax
# OUTPUT
print(grand_total)                                                  # Print the grand total amount


