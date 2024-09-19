"""
This class represents a car with attributes for color and model.
It provides methods to simulate driving and stopping the car.

Author: Akaash Deo 
"""

class Car():
    def __init__(self, color, model):
        self.color = color # Initialize the color ATTRIBUTE
        self.model = model # Initialize the model ATTRIBUTE
    
    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"{self.color} {self.model} has stopped.")
    
car1 = Car("red", "Toyota") # Creating INSTANCES of the CLASS Car
car2 = Car("blue", "honda") # Creating INSTANCES of the CLASS Car
#Accessing the Attributes
car1.drive() #Output
car2.stop() #Output"""