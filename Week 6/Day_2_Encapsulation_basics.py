
"""

Understanding Encapsulation
Encapsulation is a fundamental concept in object-oriented programming (OOP) that combines data (attributes) and methods 
(functions) into a single unit called a class. 
It also restricts direct access to some of the object's components, 
which can protect the internal state of the object from unintended or harmful modifications.

Here’s how encapsulation works and how it's implemented in Python:

Combining Data and Methods: Encapsulation bundles the data (attributes) and methods 
that operate on the data into a single class. This helps organize code and ensures that the 
data is only accessible through well-defined methods.

Data Hiding: Encapsulation allows hiding the internal state of an object from the outside. 
This means that certain data attributes are kept private and are not directly accessible from outside the class. 
Instead, the class provides methods to interact with this data safely.

Controlled Access: Encapsulation provides control over how data is accessed or modified. 
This prevents external code from changing the state of an object in unexpected ways, which helps 
maintain the integrity of the object.

Access Modifiers in Python
Python does not have explicit keywords like public, protected, or private as seen in other languages (e.g., Java or C++).
 Instead, Python uses naming conventions to indicate the intended access level:

Public: Attributes and methods that are meant to be accessible from outside the class. 
These are defined with a normal name (e.g., self.owner).

Protected: Attributes and methods that are intended to be used only within the class and its subclasses. 
These are indicated by a single underscore prefix (e.g., _self._B).

Private: Attributes and methods that are intended to be hidden from outside access. 
These are indicated by a double underscore prefix (e.g., self.__balance).

Author: Akaash Deo"""

class Person:
    def __init__(self):
        self.A = "James"       # Public attribute
        self._B = "James Bond" # Protected attribute

    def PrintName(self):
        # Method to print public and protected attributes
        print(self.A)
        print(self._B)

# Create an instance of the Person class
p = Person()

# Access public and protected attributes
print(p.A)    # Output: James (Public attribute can be accessed directly)
print(p._B)   # Output: James Bond (Protected attribute can also be accessed but should be avoided)

# Call the method to print attributes
p.PrintName() # Output: James \n James Bond

# Define the Account class with encapsulation
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner        # Public attribute: the name of the account owner
        self.__balance = balance  # Private attribute: the account balance (not directly accessible from outside)

    def deposit(self, amount):
        # Method to add money to the account
        if amount > 0:
            self.__balance += amount  # Modify the private balance attribute
            print(f"${amount} deposited.")
        else:
            print("Deposit amount must be positive.")  # Validation to ensure only positive amounts are deposited

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Modify the private balance attribute
            print(f"${amount} withdrawn.")
        else:
            print("Insufficient balance or invalid amount.")  # Validation for sufficient balance and valid withdrawal amount

    def get_balance(self):
        # Method to get the current balance
        return self.__balance  # Return the private balance attribute

### Testing the Account Class

# Create an instance of the Account class
account = Account("James", 100)

# Accessing the public attribute
print(account.owner)  # Output: James (Public attribute can be accessed directly)

# Attempt to access the private attribute (will raise an AttributeError)
try:
    print(account.__balance)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # Catch and print the error message

# Use public methods to interact with the private data
account.deposit(50)            # Output: $50 deposited.
print(account.get_balance())   # Output: 150 (Access balance using the public method)

account.withdraw(75)           # Output: $75 withdrawn.
print(account.get_balance())   # Output: 75 (Access updated balance using the public method)
