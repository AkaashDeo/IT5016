"""
Example: 

Car Class in Object-Oriented Programming

Class: Car

Attributes:

make (e.g., Toyota, Ford)
model (e.g., Corolla, Mustang)
year (e.g., 2021, 2023)

Methods:

start() – to start the car
stop() – to stop the car

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
car2.stop() #Output


"""
Real life Example 1  - Bank Account System 

Class: BankAccount

Attributes: 

account_number, 
account_holder_name, 
balance

Methods: 

deposit(amount), withdraw(amount), check_balance()

A bank uses the BankAccount class to create objects representing each customer’s account. 

Each account has its own unique account_number, belongs to a specific account_holder_name, and has a balance. 
The methods allow customers to deposit or withdraw money and check their account balance.

"""

"""

Real life Example 2 - Library Management System

Class: Book

Attributes: 

title, 
author, 
SBN, 
Availability

Methods: 

borrow(), 
return_book(), 
check_availability()

A library uses the Book class to manage its collection. 
Each book has specific details like title, author, and ISBN. 
The methods allow library staff to manage borrowing and returning of books, and to check if a book is available.

"""