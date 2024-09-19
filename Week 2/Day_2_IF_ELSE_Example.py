"""
Basic operation of the ELSE conditional statement.

Author: Akaash Deo

"""

# INPUT
a = int(input("Enter Value A: "))  # Prompt the user to enter the value for A and convert it to an integer
b = int(input("Enter Value B: "))  # Prompt the user to enter the value for B and convert it to an integer
# PROCESS & OUTPUT
"""The ELSE keyword catches anything which isn't caught by the preceding conditions."""
if b > a:  # Check if B is greater than A
    print("b is greater than a")  # If true, print this message
else:  # If the previous condition is false
    print("b is not greater than a")  # Print this message
"""ONE LINE if/else statement:"""
# INPUT
a = 2  # Set A to 2
b = 330  # Set B to 330
# PROCESS & OUTPUT
print("A") if a > b else print("B")  # Print "A" if A is greater than B, otherwise print "B"

