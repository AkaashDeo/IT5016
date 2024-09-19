"""
1. Use while loop to create a program that repeatedly asks for user input until a
correct password is entered or a maximum number of attempts is reached.
a. Write a function named `password_attempt_system()` that implements a
password attempt system.
b. Define a variable `correct_password` with the value "python123" .
c. Define an attempts variable initialized to 0.
d. Define a `max_attempts` variable set to 3.
e. Use a while loop to allow the user up to max_attempts to enter the correct
password.
f. Prompt the user to enter the password inside the loop.
g. If the entered password matches correct_password, print "Access granted!"
and exit the loop using break.
h. If the password is incorrect, increment the attempts counter and inform the
user how many attempts are left.
i. If the maximum number of attempts is reached, print "Access denied. You
have used all your attempts.".
j. Run the function and test it with different inputs to ensure it behaves as
expected.

Author: Akaash Deo
"""

def password_attempt_system():
    """
    A simple password attempt system using a while loop.
    """
    correct_password = "python123"                           # Set the correct password
    attempts = 0                                             # Initialize the number of attempts
    max_attempts = 3                                         # Set the maximum number of attempts allowed

    while attempts < max_attempts:                           # Loop until max_attempts is reached
        entered_password = input("Enter the password: ")     # Prompt user for password
        
        if entered_password == correct_password:             # Check if the entered password is correct
            print("Access granted!")                         # Inform the user access is granted
            break                                            # Exit the loop if the password is correct
        else:                                                # If the password is incorrect
            attempts += 1                                    # Increment the attempt counter
            remaining_attempts = max_attempts - attempts     # Calculate remaining attempts
            if remaining_attempts > 0:                       # Check if there are attempts left
                print(f"Incorrect password. You have {remaining_attempts} attempts left.")  # Inform user of remaining attempts
            else:                                            # If no attempts are left
                print("Access denied. You have used all your attempts.")  # Inform user access is denied

def main():
    password_attempt_system()                                # Call the password attempt system function

if __name__ == "__main__":                                   # Ensure the script runs only when executed directly
    main()                                                   # Execute the main function
