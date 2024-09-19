"""
Lab 1 - Collecting User Information

Create a Python function to get user information.
Instructions:
1. Define a Function: Name the function `collect_user_data`.
2. Initialize Unique ID Counter: (e.g., id_counter = 5000).
3. Prompt User Input:
   • Use input() to collect:
     ▪ User's Name
     ▪ User's Age
     ▪ User's Email
4. Generate Unique ID:
   • Create a unique ID by adding 1 to the current counter value.
   • Return the updated counter and the generated ID.
5. Return and Display User Information:
   • Return the updated counter and the generated ID.
   • Print the information in a formatted manner.

Author: Akaash Deo
"""

def collect_user_data(id_counter):
    
    # Prompt the user for their information
    name = input("User Name: ")              # Collect user's name
    age = input("User Age: ")                # Collect user's age
    email = input("User Email: ")            # Collect user's email

    # Generate a unique ID
    unique_id = id_counter + 1               # Increment the ID counter
    id_counter = unique_id                   # Update the ID counter

    # Display the collected user information
    print(f"\nUser Information:")
    print(f"Name: {name}")                   # Display user's name
    print(f"Age: {age}")                     # Display user's age
    print(f"Email Address: {email}")         # Display user's email
    print(f"Unique ID: {unique_id}")         # Display the unique ID

    return id_counter                        # Return the updated counter

collect_user_data(5000)                      # Call the function with an initial counter value

