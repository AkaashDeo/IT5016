"""
Collect user information and generate a unique ID

Author: Akaash Deo
"""

def collect_user_id(id_counter):
    # Input: Gather user details
    name = input("Name: ")                     # Prompt user for their name
    age = input("Age: ")                       # Prompt user for their age
    email = input("Email Address: ")           # Prompt user for their email address

    # Process: Generate a unique ID
    unique_id = id_counter + 1                 # Increment the ID counter by 1

    # Output: Display collected information
    print(f"User Information:")
    print(f"Name: {name}")                     # Display user's name
    print(f"Age: {age}")                       # Display user's age
    print(f"Email Address: {email}")           # Display user's email
    print(f"Unique ID: {unique_id}")           # Display the generated unique ID

    return                                     # End of function

def main():
    collect_user_id(5000)                      # Call the function with an initial ID counter

main()                                         # Run the main function


"""
Alternative implementation: Collect User ID

Author: Akaash Deo
"""

def collect_user_id(id_counter):
    # Input: Gather user details
    name = input("Name: ")                     # Prompt user for their name
    age = input("Age: ")                       # Prompt user for their age
    email = input("Email Address: ")           # Prompt user for their email address

    # Process: Generate a unique ID
    unique_id = id_counter + 1                 # Increment the ID counter by 1

    # Output: Display collected information
    print(f"User Information:")
    print(f"Name: {name}")                     # Display user's name
    print(f"Age: {age}")                       # Display user's age
    print(f"Email Address: {email}")           # Display user's email
    print(f"Unique ID: {unique_id}")           # Display the generated unique ID

    return                                     # End of function

def main():
    collect_user_id(5000)  # Call the function with an initial ID counter

# Run the main function
main()


"""Alternative version to demonstrate collecting static user data"""

def collect_user_data():
    id_counter = 5000                          # Initial ID counter

    prompt = "Enter User Information:"
    print(prompt)                              # Display prompt message

    # Input: Static user data
    user_name = str("James")                   # Static name input
    print("Name:", user_name)                  # Display user's name

    user_age = int(32)                         # Static age input
    print("Age:", user_age)                    # Display user's age

    user_email = str("j.b@gmail.com")          # Static email input
    print("Email address:", user_email)        # Display user's email
    
    # Process: Generate a unique ID
    unique_id = id_counter + 1                 # Increment the ID counter by 1
    print("Unique ID:", unique_id)             # Display the generated unique ID

def main():
    collect_user_data()                        # Call the function to display user data

# Run the main function
main()

# Lecturer's working version

def collect_user_data(id_counter):
    """
    Collects user information and generates a unique ID.

    Args:
        id_counter (int): The starting value for the unique ID.
    """
    # Input: Gather user details
    name = input("Name: ")                     # Prompt user for their name
    age = input("Age: ")                       # Prompt user for their age
    email = input("Email: ")                   # Prompt user for their email address

    # Process: Generate a unique ID
    unique_id = id_counter + 1                 # Increment the ID counter by 1
    id_counter = unique_id                     # Update id_counter (though not used further)

    # Output: Display collected information
    print(f"User Information: ")
    print(f"Name: {name}")                     # Display user's name
    print(f"Age: {age}")                       # Display user's age
    print(f"Email address: {email}")           # Display user's email
    print(f"Unique ID: {unique_id}")           # Display the generated unique ID

    return id_counter, unique_id, name, age, email  # Return all relevant information

def main():
    """
    Main function to execute the user information collection.
    """
    collect_user_data(5000)                    # Call the function with an initial ID counter

main()                                         # Run the main function

