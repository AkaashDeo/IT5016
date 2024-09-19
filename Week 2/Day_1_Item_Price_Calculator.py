"""
- Calculate 3 variable: item1, item2, item3
- Calculate Subtotal as the result variable, the expression is subtotal = item1+item2+item3
- Calculate Salestax to be the result of the expression Subtotal * 0.15.
- Calculate Total = Subtotal + Salestax
- Display the total
- Run your program with your test data with 10,20 and 30 and check your output should be : "Your purchase total is $69"

Author: Rajiv Akaash Deo
"""

# INPUT
item1 = float(input("Enter the price for item1:"))      # Prompt the user to enter the price for item1 and convert it to a float
item2 = float(input("Enter the price for item2:"))      # Prompt the user to enter the price for item2 and convert it to a float
item3 = float(input("Enter the price for item3:"))      # Prompt the user to enter the price for item3 and convert it to a float
# PROCESS
subTotal = item1 + item2 + item3                        # Calculate the subtotal by summing the prices of the three items
salesGST = subTotal * 0.15                              # Calculate the sales tax (GST) as 15% of the subtotal
total = subTotal + salesGST                             # Calculate the total by adding the subtotal and the sales tax
# OUTPUT
print("Your purchase total is $", total, sep="")        # The sep="" parameter ensures there is no space between the dollar sign and the total amount.



























"""
- Calculate 3 variable: item1, item2, item3
- Calculate Subtotal as the result variable, the expression is subtotal = item1+item2+item3
- Calculate Salestax to be the result of the expression Subtotal * 0.15.
- Calculate Total = Subtotal + Salestax
- Display the total
- Run your program with your test data with 10,20 and 30 and check your output should be : "Your purchase total is $69"

Author: Rajiv Akaash Deo"""

item1 = float(input("Enter the price for item 1:\n"))
item2 = float(input("Enter the price for item 2:\n"))
item3 = float(input("Enter the price for item 3:\n"))

subtotal = item1 + item2 + item3

salestax = subtotal * 0.15

total = salestax + subtotal

print("$",total)

