
"""
Class Practice:

Create a `vehicle` class with methods for starting and stopping. 
Create a `car` class that inherits from `Vehicle` and adds a method for honking the horn.

Author: Rajiv Deo
"""

# Define the base class Vehicle
class Vehicle:
    def __init__(self) -> None:             # Constructor method for Vehicle class
        pass                                # No initialization needed here

    def start(self):                        # Method to start the vehicle
        print("Vehicle has started.")       # Output indicating the vehicle has started
    
    def stop(self):                         # Method to stop the vehicle
        print("Vehicle has stopped.")       # Output indicating the vehicle has stopped

# Define the derived class Car that inherits from Vehicle
class Car(Vehicle):
    def toot(self):                         # Method specific to Car class to honk the horn
        print("Honk! Honk!")                # Output indicating the horn is honking

# Create an instance of the Car class
my_car = Car()                              # Initialize a Car object

# Call methods inherited from Vehicle and those specific to Car
my_car.start()                              # Output: Vehicle has started.
my_car.toot()                               # Output: Honk! Honk!
my_car.stop()                               # Output: Vehicle has stopped.

"""
Explanation of the Code

Base Class (Vehicle):
- The Vehicle class is the base class in this example. 
- It defines two methods:
  - start(): Prints a message indicating that the vehicle has started.
  - stop(): Prints a message indicating that the vehicle has stopped.
- The __init__ method is the constructor, but in this case, it doesn't initialize any attributes (it's just a placeholder).

Derived Class (Car):
- The Car class inherits from the Vehicle class. 
- This means that Car automatically gains the start() and stop() methods from Vehicle.
- The Car class adds an additional method:
  - toot(): Prints a message to simulate honking the horn.
- By inheriting from Vehicle, the Car class does not need to re-implement the start() and stop() methods; it can use them directly.

Creating and Using an Instance:
- An instance of Car is created with my_car = Car().
- The instance my_car can call methods from both Vehicle and Car:
  - my_car.start() calls the inherited start() method from Vehicle.
  - my_car.toot() calls the toot() method defined in Car.
  - my_car.stop() calls the inherited stop() method from Vehicle.

Summary:
- In this example:
  - Inheritance allows Car to reuse and extend the functionality of Vehicle.
  - The Car class inherits the start() and stop() methods from Vehicle, demonstrating code reuse.
  - The Car class introduces a new method toot() that is specific to cars, showcasing how derived classes can extend the functionality of base classes.
"""
