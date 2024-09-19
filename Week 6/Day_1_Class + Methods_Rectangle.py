"""
The following shows how to use a function and enter values.

Author: Akaash Deo
"""

# Define the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        # Constructor method to initialize Rectangle attributes
        self.width = width  # Initialize the width attribute
        self.height = height  # Initialize the height attribute

    def area(self):
        # Method to calculate the area of the rectangle
        return self.width * self.height  # Return the product of width and height

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle
        return 2 * (self.width + self.height)  # Return twice the sum of width and height

# Create an instance of the Rectangle class with width 4 and height 5
rect = Rectangle(4, 5)

# Print the area of the rectangle
print(f"Area: {rect.area()}")  # Call the area method and print the result

# Print the perimeter of the rectangle
print(f"Perimeter: {rect.perimeter()}")  # Call the perimeter method and print the result

"""
Explanation of Each Line

Class Definition (Rectangle):
class Rectangle:: Defines a new class named Rectangle.

Constructor Method (__init__):
def __init__(self, width, height):: This is the constructor method for initializing new instances of Rectangle.
self.width = width: Assigns the width parameter to the instance variable self.width.
self.height = height: Assigns the height parameter to the instance variable self.height.

Method (area):
def area(self):: Defines a method named area that calculates the area of the rectangle.
return self.width * self.height: Returns the product of width and height, which is the area of the rectangle.

Method (perimeter):
def perimeter(self):: Defines a method named perimeter that calculates the perimeter of the rectangle.
return 2 * (self.width + self.height): Returns twice the sum of width and height, which is the perimeter of the rectangle.

Creating an Instance:
rect = Rectangle(4, 5): Creates an instance of the Rectangle class named rect with width set to 4 and height set to 5.

Printing Results:
print(f"Area: {rect.area()}"): Calls the area method on the rect instance and prints the calculated area.
print(f"Perimeter: {rect.perimeter()}"): Calls the perimeter method on the rect instance and prints the calculated perimeter.

Summary
This code defines a Rectangle class with methods to calculate the area and perimeter of the rectangle. 
The class uses attributes width and height initialized through the constructor. 
The methods area and perimeter perform calculations based on these attributes. 
An instance of Rectangle is created and its methods are used to print the area and perimeter."""