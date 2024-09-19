""" 1.1: Create a Class to Encapsulate Common Information Using the Object-Oriented Concept

Author: Akaash Deo"""

# Example: A `Person` class

class Person:
    """Class to represent a person with basic information."""
    
    def __init__(self, name, age, address):
        """Initialize common attributes.
        
        Arguments:
            name (str): The name of the person.
            age (int): The age of the person.
            address (str): The address of the person.
        """
        self.name = name          # Assign the name to the instance variable.
        self.age = age            # Assign the age to the instance variable.
        self.address = address    # Assign the address to the instance variable.

    def birthday(self):
        """Increment age by 1."""
        self.age += 1            # Increase the age by one year.

    def move(self, new_address):
        """Update address to a new location."""
        self.address = new_address  # Set the new address.

    def display_info(self):
        """Display the person's information."""
        print(f"Name: {self.name}")          # Print the person's name.
        print(f"Age: {self.age}")            # Print the person's age.
        print(f"Address: {self.address}")    # Print the person's address.

    def is_adult(self):
        """Check if the person is considered an adult (18 years or older)."""
        return self.age >= 18              # Return True if age is 18 or more, otherwise False.

# Explanation:
# The `Person` class encapsulates common information about a person, including their name, age, and address.
# The `__init__` method initializes these attributes when a new instance of the class is created.

# 1.4: Test Your Software by Creating Different Instances and Displaying Their Results

# Example: Testing the `Person` class

# Create instances of Person
person1 = Person("Alice", 30, "123 Main St")  # Instance of Person for Alice
person2 = Person("Bob", 17, "456 Elm St")     # Instance of Person for Bob

# Display information for person1
person1.display_info()                           # Call display_info method to show Alice's details.
print(f"Is {person1.name} an adult? {'Yes' if person1.is_adult() else 'No'}")  # Check if Alice is an adult.

# Test methods for person1
person1.birthday()                               # Increment Alice's age by 1.
person1.move("789 Oak St")                       # Update Alice's address.
person1.display_info()                           # Show updated information for Alice.

# Display information for person2
person2.display_info()                           # Call display_info method to show Bob's details.
print(f"Is {person2.name} an adult? {'Yes' if person2.is_adult() else 'No'}")  # Check if Bob is an adult.

# 2.1: Identify and Explain the Different Stages of the Software Development Life Cycle (SDLC)

# 1. Planning 
"""Overview: Define the scope and objectives of the project.
- Determine that you need a `Person` class to manage personal information and perform certain tasks."""

# 2. Requirement Analysis
"""Overview: Gather and document the requirements.
- Identify that the `Person` class should include attributes for name, age, and address and methods for updating 
information and displaying results."""

# 3. Design
"""Overview: Create a blueprint for the class.
- Design the `Person` class with an `__init__` method to initialize attributes and methods for managing and displaying information."""

# 4. Implementation
"""Overview: Write the actual code based on the design.
- Implement the `Person` class in Python with the methods described above."""

# 5. Testing
"""Overview: Verify that the code works correctly.
- Example: Create instances of `Person`, test the methods (`birthday()`, `move()`, `display_info()`, 
and `is_adult()`), and ensure they behave as expected."""

# 6. Maintenance
"""Overview: Make updates and fix issues.
- If users report bugs or request new features (e.g., adding a phone number attribute), update the `Person` class accordingly."""

# Explanation: Following these SDLC stages ensures that the code is well-structured, meets requirements, is thoroughly tested, and is maintained effectively throughout its lifecycle.
