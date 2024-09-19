

"""
Calculate the radius of a circle, given the area.

This program prompts the user to input the area of a circle and calculates the radius
using the formula: radius = sqrt(area / π). It then prints the calculated radius.

Author: Rajiv Deo
"""
# INPUT
import math                                          # Import the math module to access mathematical functions and constants
area = float(input("Enter the area value: "))        # Prompt the user to input the area value and convert it to a float
# PROCESS
radius = math.sqrt(area / math.pi)                   # Calculate the radius using the formula radius = sqrt(area / π)
# OUTPUT
print("Radius of circle:", radius)                   # Print the calculated radius of the circle
