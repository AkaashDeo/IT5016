class Person:
    """
    Mock Exam Practice.
    
    Akaash Deo
    """
    
    
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

# Test Your Software by Creating Different Instances and Displaying Their Results

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
