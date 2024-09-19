
"""
Code calculates the area of a circle given its radius

Author: Rajiv Deo
"""

# INPUT                                           
radius = float(input("Enter the radius: "))       # Prompt the user to enter the radius of the circle, The input() function reads the input as a string, and float() converts it to a floating-point number.
pi = 3.14159265359                                # Assign the value of pi, close to the mathematical constant π (pi), which is approximately 3.14159265359.
# PROCESS
area = pi * radius ** 2                           # Calculate the area of the circle using the formula: Area = π * radius ** 2
# OUTPUT
print("Area of a circle is", area)                # Output the result. Print "Area of a circle is " followed by the computed area.

