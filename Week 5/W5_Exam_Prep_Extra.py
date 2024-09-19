"""
Exam: Prep: Collect User Id

Author: Akaash Deo
"""

def collect_user_id(id_counter):
    """
    Collects user information including name, age, and email address,
    and generates a unique ID.

    Parameters:
        id_counter (int): The starting point for generating unique IDs.
    """
    # Prompt user for input
    name = input("Name: ")                  # Input user's name
    age = input("Age: ")                    # Input user's age
    email = input("Email Address: ")        # Input user's email address

    unique_id = id_counter + 1              # Generate a unique ID

    # Print the collected user information
    print(f"User Information:")
    print(f"Name: {name}")                   # Output user's name
    print(f"Age: {age}")                     # Output user's age
    print(f"Email Address: {email}")         # Output user's email address
    print(f"Unique ID: {unique_id}")         # Output the unique ID
    return

def main():
    """Main function to start the user ID collection process."""
    collect_user_id(5000)                   # Start collecting user ID with a base counter

main()  # Call the main function


def collect_user_data():
    """
    Collects and displays user information with a preset example.

    This function does not take any parameters and uses predefined values.
    """
    id_counter = 5000                        # Initialize the ID counter

    prompt = "Enter User Information:"
    print(prompt)                            # Print the prompt for user information

    user_name = str("James")                 # Predefined user name
    print("Name:", user_name)                # Output predefined user name

    user_age = int(32)                       # Predefined user age
    print("Age:", user_age)                  # Output predefined user age

    user_email = str("j.b@gmail.com")        # Predefined user email
    print("Email address:", user_email)      # Output predefined user email
    
    unique_id = id_counter + 1               # Generate a unique ID
    print("Unique_ID:", unique_id)           # Output the unique ID

def main():
    """Main function to call the user data collection."""
    collect_user_data()                      # Call the user data collection function

main()  # Call the main function


# LECTURER'S WORKING.

def collect_user_data(id_counter):
    """
    Collects user data including name, age, and email, and generates a unique ID.

    Parameters:
        id_counter (int): The starting point for generating unique IDs.

    Returns:
        tuple: Updated ID counter, unique ID, name, age, and email.
    """
    # Prompt user for input
    name = input("Name: ")                   # Input user's name
    age = input("Age: ")                     # Input user's age
    email = input("Email: ")                 # Input user's email address

    unique_id = id_counter + 1               # Generate a unique ID
    id_counter = unique_id                    # Update the ID counter

    # Print the collected user information
    print(f"User Information: ")
    print(f"Name: {name}")                   # Output user's name
    print(f"Age: {age}")                     # Output user's age
    print(f"Email address: {email}")         # Output user's email address
    print(f"Unique ID: {unique_id}")         # Output the unique ID

    return id_counter, unique_id, name, age, email  # Return collected information

def main():
    """Main function to start the user data collection process."""
    collect_user_data(5000)                  # Start collecting user data with a base counter

main()  # Call the main function
