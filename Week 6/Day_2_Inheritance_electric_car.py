# Inheritance Concept

"""
Inheritance is a fundamental concept in object-oriented programming (OOP) where a new class (called the derived or child class) 
is based on an existing class (called the base or parent class). The derived class inherits attributes and methods from the base 
class and can also introduce its own attributes and methods or override existing ones.

The key benefits of inheritance include:

Code Reusability: You can reuse the code from the base class in the derived class.

Extensibility: You can extend the base class's functionality in the derived class.

Maintainability: It helps in organizing code in a hierarchical manner, making it easier to manage and maintain."""


# Task 1

"""
Task 1
1. Create a new class `ElectricCar` that inherits from the Car class (from week 6
Lab 1 Task 3 and 4).

2. Add an additional attribute to `ElectricCar`:

- battery_capacity (integer)

3. Override the `display_info` method in `ElectricCar` to include battery capacity
information.

4. Create an instance of `ElectricCar` and call its methods to test functionality.

Author: Rajiv Deo"""


# Define a base class Car
class Car:
    def __init__(self, color, model, year):
        self.color = color          # Initialize the color of the car
        self.model = model          # Initialize the model of the car
        self.year = year            # Initialize the year of manufacture

    def drive(self):
        # Method to simulate driving the car
        print(f"The {self.color} {self.model} is driving.")

    def stopped(self):
        # Method to simulate the car stopping
        print(f"The {self.color} {self.model} has stopped.")

    def display_info(self):
        # Method to display basic information about the car
        print(f"Car Info: {self.year} {self.color} {self.model}")

# Define a derived class ElectricCar that inherits from Car
class ElectricCar(Car):
    def __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)  # Call the __init__ method of the base class Car
        self.battery_capacity = battery_capacity  # Initialize the battery capacity specific to ElectricCar

    def display_info(self):
        # Override the display_info method to include battery capacity
        super().display_info()  # Call the display_info method of the base class Car
        print(f"Battery Capacity: {self.battery_capacity} kWh")  # Display battery capacity

# Create an instance of ElectricCar
my_electric_car = ElectricCar("white", "Tesla Model 3", 2022, 75)

# Call methods on the ElectricCar instance
my_electric_car.drive()           # Call the drive method inherited from Car
my_electric_car.stopped()         # Call the stopped method inherited from Car
my_electric_car.display_info()    # Call the overridden display_info method in ElectricCar
