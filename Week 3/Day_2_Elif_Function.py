"""
The following shows how to use elif function.

Author: Akaash Deo
"""

def what_to_do_now():                              # Function to determine an action based on user choice.
    message = "Time to"                            # Base message to be used in the output.
    prompt = "Enter Selection (1, 2 or 3):"        # Prompt message for user input.
    user_choice = int(input(prompt))               # Get user input and convert to an integer.

    if user_choice == 1:                           # Check if user selected 1.
        print(message, "eat")                      # Suggest eating.
    elif user_choice == 2:                         # Check if user selected 2.
        print(message, "play")                     # Suggest playing.
    elif user_choice == 3:                         # Check if user selected 3.
        print(message, "sleep")                    # Suggest sleeping.
    else:                                          # Handle invalid selections.
        print("Incorrect selection")               # Inform the user of the incorrect selection.

what_to_do_now()                                   # Execute the function.
