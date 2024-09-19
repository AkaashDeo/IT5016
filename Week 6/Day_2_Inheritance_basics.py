# Filename: inheritance_example.py

"""
The following code shows how to use the Inheritance function

Author: Akaash Deo
"""

class Animal:                               # Define the parent class
    def __init__(self, name):               # Constructor for the Animal class
        self.name = name                    # Initialize the name attribute

    def speak(self):                        # Method to make the animal speak
        print(f"{self.name} makes a sound.")# Output the sound of the animal

class Dog(Animal):                          # Define the child class inheriting from Animal
    def bark(self):                         # Method specific to the Dog class
        print(f"{self.name} barks.")        # Output the barking sound

# Create an instance of the Dog class
my_dog = Dog("Buddy")                       # Initialize a Dog object with the name "Buddy"

# Call the speak method from the parent class
my_dog.speak()                              # Outputs: Buddy makes a sound.

# Call the bark method from the Dog class
my_dog.bark()                               # Outputs: Buddy barks.
