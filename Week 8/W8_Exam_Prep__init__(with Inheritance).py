
"""
Class Inheritance Example.

Author: Akaash Deo
"""

class IT5010: 
    def __init__(self, name):                     # Constructor: Initializes the name parameter
        self.name = name                           # Assigns the name parameter to the instance variable
        print("This is the PARENT Class")         # Outputs a message indicating the parent class

class Network_diagram(IT5010):                    # Inherits from the IT5010 class
    def __init__(self, name):                      # Constructor: Initializes the name parameter for the child class
        IT5010.__init__(self, name)                # Calls the parent class constructor to initialize the name
        print('This is the Child Class')           # Outputs a message indicating the child class
        self.name = name                           # Assigns the name parameter to the instance variable

object1 = Network_diagram('Akaash')               # Creates an instance of Network_diagram with the name 'Akaash'
