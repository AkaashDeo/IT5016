"""
This program calculates the area of rectangles of different sizes.
It demonstrates how to use basic arithmetic operations and string concatenation to display results.

Author: Akaash Deo
"""

# INPUT
width = 5                                                                                               # Set the width of the rectangle.
height = 10                                                                                             # Set the height of the rectangle.
# PROCESS
areas = width * height                                                                                  # Calculate the area of the rectangle by multiplying width and height.
output = "Area of the rectangle with width " + str(width) + ", and height being " + str(height) + ":"   # Prepare the output message
# OUTPUT
print(output, "Total Area:", areas)                                                                     # Print the formatted output message along with the calculated area.
