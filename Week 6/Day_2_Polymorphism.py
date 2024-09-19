"""
Polymorphism

Polymorphism is a concept in object-oriented programming that allows different classes to be treated through the same 
interface, even though they may implement the interface in different ways. 

It enables objects of different classes to respond to the same method or function call with their own specific behavior.

Think of it like a universal remote control that can operate various devices, like a TV, a fan, and a light. 
Even though you use the same button (e.g., turn_on()), each device responds in its unique way:

TV: Turns on the TV screen.
Fan: Starts spinning.
Light: Lights up.
"""

# Define the base class
class Device:
    def turn_on(self):  # Base method that will be overridden by subclasses
        pass  # This method is a placeholder and does not perform any action in the base class

# Define the Tv class that inherits from Device
class Tv(Device):
    def turn_on(self):  # Override the turn_on method to provide specific functionality for TV
        return "TV is now on."  # Returns a string indicating the TV is turned on

# Define the Fan class that inherits from Device
class Fan(Device):
    def turn_on(self):  # Override the turn_on method to provide specific functionality for Fan
        return "Fan is now spinning."  # Returns a string indicating the fan is spinning

# Define the Light class that inherits from Device
class Light(Device):
    def turn_on(self):  # Override the turn_on method to provide specific functionality for Light
        return "Light is now on."  # Returns a string indicating the light is turned on

# Function to demonstrate polymorphism
def activate_device(device):  # This function calls the turn_on method on any device object passed to it
    print(device.turn_on())  # Executes the turn_on method and prints the result

# Create instances for each device
tv = Tv()      # Create an instance of the Tv class
fan = Fan()    # Create an instance of the Fan class
light = Light() # Create an instance of the Light class

# Use polymorphism to activate each device
activate_device(tv)   # Output: TV is now on. (Calls the turn_on method for the Tv instance)
activate_device(fan)  # Output: Fan is now spinning. (Calls the turn_on method for the Fan instance)
activate_device(light) # Output: Light is now on. (Calls the turn_on method for the Light instance)

"""
Explanation of Each Section

Base Class Definition:
- class Device: Defines a base class Device.
- def turn_on(self): A placeholder method that will be overridden in derived classes. 
It doesn’t perform any action in the base class and is meant to be a common interface for all devices.

Derived Classes:
- class Tv(Device): Defines a class Tv that inherits from Device.
- def turn_on(self): Overrides the turn_on method to provide specific behavior for turning on a TV.
- class Fan(Device): Defines a class Fan that inherits from Device.
- def turn_on(self): Overrides the turn_on method to provide specific behavior for starting the fan.
- class Light(Device): Defines a class Light that inherits from Device.
- def turn_on(self): Overrides the turn_on method to provide specific behavior for turning on the light.

Polymorphism Function:
- def activate_device(device): A function that accepts a Device object and calls its turn_on method.
- print(device.turn_on()): Calls the turn_on method on the device object, demonstrating polymorphism.

Creating Instances:
- tv = Tv(), fan = Fan(), light = Light(): Creates instances of Tv, Fan, and Light.

Using Polymorphism:
- activate_device(tv), activate_device(fan), activate_device(light): Calls activate_device with different device instances. 
Each call to activate_device uses the specific turn_on method of the provided device, demonstrating how 
polymorphism allows the same method name to have different behaviors.

Summary:
- Polymorphism allows different objects (e.g., TV, Fan, Light) to respond to the same method (turn_on()) in their own way.
- Base Class (Device) provides a common interface with a method turn_on that is overridden in derived classes.
- Derived Classes (Tv, Fan, Light) provide specific implementations of the turn_on method.
- The activate_device function demonstrates polymorphism by calling the turn_on method on different types of devices, 
showing how each device type responds according to its own implementation of the method."""
