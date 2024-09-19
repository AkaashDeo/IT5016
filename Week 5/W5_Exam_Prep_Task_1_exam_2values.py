"""
Two parameters. These parameters will be:

id_counter : to keep track of the current unique ID value.
initial_value : a starting value for the unique ID generation. For simplicity, it can represent the 
initial counter value.

Author: Akaash Deo
"""

def collect_user_data(id_counter, initial_value):
    # Prompt user for input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    
    # Generate a unique ID by adding the initial value to the current counter
    unique_id = initial_value + id_counter
    
    # Update the counter
    id_counter += 1
    
    # Print the user information in a formatted manner
    print(f"User Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Unique ID: {unique_id}")
    
    # Return the updated counter and the generated ID
    return id_counter, unique_id

# Example usage:
current_counter = 5000
starting_value = 100  # Initial value for unique ID generation
current_counter, new_id = collect_user_data(current_counter, starting_value)
print(f"Updated Counter: {current_counter}")

