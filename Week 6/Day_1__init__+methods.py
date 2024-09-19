
"""
1. Define a Car class with the following attributes:
o color (string)
o model (string)
o year (integer)
2. Implement the __init__ method to initialize these attributes.
3. Create an instance of the Car class with your chosen values for color, model,
and year.
4. Print the attributes of the Car instance to verify they are set correctly.

Author: Akaash Deo
"""

# Define the Car class
class Car:
    def __init__(self, color, model, year):
        # Constructor method to initialize the Car attributes
        self.color = color                    # Initialize the color attribute
        self.model = model                    # Initialize the model attribute
        self.year = year                      # Initialize the year attribute

    def park(self):
        # Method to print a message about the car being parked
        print(f"Elon Musk is driving the {self.color} {self.model} which was released in {self.year}")

# Create an instance of the Car class with specific attributes
the_car = Car("black", "Tesla Model S", 2023)

# Call the park method on the_car instance
the_car.park()

# Define the Car class again with additional methods
class Car:
    def __init__(self, color, model, year):
        # Constructor method to initialize the Car attributes
        self.color = color                     # Initialize the color attribute
        self.model = model                     # Initialize the model attribute
        self.year = year                       # Initialize the year attribute

    def drive(self):
        # Method to print a message about the car driving
        print(f"The {self.color} {self.model} is driving.")

    def stopped(self):
        # Method to print a message about the car stopping
        print(f"The {self.color} {self.model} has stopped.")
    
    def display_info(self):
        # Method to print the car's information
        print(f"Car Info: {self.year} {self.color} {self.model}")

# Create a new instance of the Car class with different attributes
the_car = Car("blue", "Ford Mustang", 2021)

# Call methods on the_car instance to display car details and actions
the_car.drive()                                 # Output: The blue Ford Mustang is driving.
the_car.stopped()                               # Output: The blue Ford Mustang has stopped.
the_car.display_info()                          # Output: Car Info: 2021 blue Ford Mustang

"""

Explanation of Each Section

First Definition of the Car Class:
class Car:: Defines the Car class.

def __init__(self, color, model, year):: Constructor method initializes attributes color, model, and year.

self.color = color: Sets the color attribute.
self.model = model: Sets the model attribute.
self.year = year: Sets the year attribute.

def park(self):: Method to print a message about the car being parked.
print(f"Elon Musk is driving the {self.color} {self.model} which was released in {self.year}"): 
Prints a message using the car's attributes.

Creating an Instance:
the_car = Car("black", "Tesla Model S", 2023): Creates an instance of Car with specified attributes.
the_car.park(): Calls the park method to print a message about the car.

Second Definition of the Car Class:
The Car class is redefined with additional methods: drive, stopped, and display_info.
def drive(self):: Method to print a message about the car driving.
def stopped(self):: Method to print a message about the car stopping.
def display_info(self):: Method to print detailed information about the car.

Creating a New Instance:
the_car = Car("blue", "Ford Mustang", 2021): Creates a new instance of Car with different attributes.
the_car.drive(): Calls the drive method.
the_car.stopped(): Calls the stopped method.
the_car.display_info(): Calls the display_info method to print the car's details.

Summary
This code demonstrates how to define a class with attributes and methods, create instances of the class, 
and interact with those instances. The Car class is first defined with basic attributes and a single method, 
then redefined to include additional functionality. Each method performs specific actions or prints 
information based on the instance's attributes."""