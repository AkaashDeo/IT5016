"""
Lab 1 - Collecting User Information
Create a Python function to get user information.
Instructions:
1. Define a Function: Name the function `collect_user_data`.
2. Initialize Unique ID Counter: (e.g., id_counter = 5000).
3. Prompt User Input:
   - Use input() to collect:
     - User's Name
     - User's Age
     - User's Email
4. Generate Unique ID:
   - Create a unique ID by adding 1 to the current counter value.
   - Return the updated counter and the generated ID.
5. Return and Display User Information:
   - Return the updated counter and the generated ID.
   - Print the information in a formatted manner.

Author: Akaash Deo
"""

def collect_user_data(id_counter):
    # Prompt user for input
    name = input("User Name: ")
    age = input("User Age: ")
    email = input("User Email Address: ")

    # Generate a unique ID by adding 1 to the current counter value
    unique_id = id_counter + 1
    
    # Update the counter
    id_counter = unique_id

    # Print the user information in a formatted manner
    print(f"User Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email Address: {email}")
    print(f"Unique ID: {unique_id}")

    return id_counter                                       # Return the updated counter

def main():
    current_counter = 5000                                  # Initialize the ID counter
    updated_counter = collect_user_data(current_counter)    # Call the function and get the updated counter
    print(f"Updated ID Counter: {updated_counter}")         # Display the updated counter

main()                                                      # Execute the main function

