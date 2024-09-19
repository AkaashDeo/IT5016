
# Encapsulation Concept
"""
Encapsulation is the concept of wrapping data (attributes) and methods (functions) that operate on the data into a 
single unit or class. 

It helps in:

Hiding Internal State: By making attributes private, you can prevent external code from directly accessing or modifying them.

Providing Controlled Access: Public methods (getters and setters) are used to interact with the private data, allowing 
control over how the data is accessed or modified."""

# Task 2 - Banking System with Encapsulation
"""

Define the Account Class
Use the provided Account class definition. The class has the following features:
• Attributes:
- owner (public): The name of the account owner.
- __balance (private): The account balance.
• Methods:
- deposit(amount): Adds money to the account if the amount is positive.
- withdraw(amount): Withdraws money from the account if there is
sufficient balance.
- get_balance(): Returns the current balance.

Author: Akaash Deo
"""
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
