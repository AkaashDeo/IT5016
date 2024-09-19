"""
Calculate the total wholesale cost for 60 copies of a book.

Author: Akaash Deo
"""

# INPUT
# Constants for the book's pricing
cover_price = 24.95                                                       # The cover price of one book
discount_rate = 0.40                                                      # Discount rate
num_copies = 60                                                           # Number of copies to purchase
# PROCESS
# Calculate the discounted price for one book
discounted_amount_one_book = cover_price * discount_rate                  # Calculate discount amount
total_after_discount_one_book = cover_price - discounted_amount_one_book  # Calculate total price after discount
total_for_all_books = total_after_discount_one_book * num_copies          # Calculate total price for all books
# Calculate shipping costs
shipping_costs = 3 + 0.75 * (num_copies - 1)                              # Base shipping cost plus per-copy shipping
# Calculate the final total cost
total = total_for_all_books + shipping_costs                              # Add book cost and shipping cost
# OUTPUT
print(f"Total wholesale cost for 60 copies is ${total:.2f}")              # Print the total cost with 2 decimal places



"""Function to print "Happy Birthday" multiple times"""

# Example 1: Happy Birthday without using functions
print("Happy Birthday to you")
print("Happy Birthday to you")
print("Happy Birthday to you")

# Define a function for reusability
def happy_birthday():
    """
    Prints "Happy Birthday" three times.
    """
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday to you")

# Call the happy birthday function
happy_birthday()                                                          # Function call
print()                                                                   # Print a new line for spacing

# Function to print Happy Birthday with a name
def happy_birthday(name):
    """
    Prints a personalized happy birthday message.
    
    Args:
        name (str): The name of the person celebrating their birthday.
    """
    print(f"Happy Birthday to {name}")
    print(f"Happy Birthday to {name}")
    print(f"Happy Birthday to {name}")

# Call the function with different names
happy_birthday("Jess")                                                     # Function call with name
happy_birthday("Aiden")
happy_birthday("Vasiti")

print()                                                                    # Print a new line for spacing

# Function to print Happy Birthday with name and age
def happy_birthday(name, age):
    """
    Prints a personalized happy birthday message with age.
    
    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """
    print(f"Happy Birthday to {name}")
    print(f"You are now {age} years old")

# Call the function with names and ages
happy_birthday("Boss", 20)                                                  # Function call with name and age
happy_birthday("Minty", 30)
happy_birthday("Sinario", 50)

print()                                                                     # Print a new line for spacing

# User input for names and ages
def happy_birthday(name, age):
    """
    Prints a birthday message with user-provided name and age.
    
    Args:
        name (str): The name of the person.
        age (int): The age of the person.
    """
    print(f"Happy Birthday to {name}")
    print(f"You are now {age} years old")

# Get user input for names and ages, and call the function
happy_birthday(str(input("Enter name 1: ")), 100)                             # User input for name and age
happy_birthday(str(input("Enter name 2: ")), 40)
happy_birthday(str(input("Enter name 3: ")), 100)

print()                                                                       # Print a new line for spacing
