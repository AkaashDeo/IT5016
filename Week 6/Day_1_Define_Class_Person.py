"""
The following defines a 'Person' Class

Author: Akaash Deo"""

# Define the Person class
class Person:
    def __init__(self, name, age):
        # Constructor method to initialize Person attributes
        self.name = name  # Initialize attribute for the person's name
        self.age = age    # Initialize attribute for the person's age
    
    def greet(self):
        # Method to print a greeting message including the person's name and age
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class with name "James" and age 30
person1 = Person("James", 30)

# Call the greet method on the person1 instance to print the greeting message
person1.greet()
