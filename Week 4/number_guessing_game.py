"""
The following function prompts the user to guess a hidden number until they guess correctly.
It provides feedback on whether the guess is too high or too low and tracks the number of attempts made.
Author: Rajiv Deo
"""

import random                                                    # Import the random module to generate a random number.

def user_number_guess(computer_num):
    prompt = "Enter your guess (1 - 99): "                       # Prompt for user input
    num_guesses = 0                                              # Initialize the number of guesses
    number = 0                                                   # Initialize the user's guess

    while number != computer_num:                                # Continue until the correct number is guessed
        number = int(input(prompt))                              # Get the user's guess
        num_guesses += 1                                         # Increment the number of guesses

        if number < computer_num:
            print("Too low")                                     # Feedback if the guess is too low
        elif number > computer_num:
            print("Too high")                                    # Feedback if the guess is too high
        else:
            print(f"Correct! Number of guesses: {num_guesses}")  # Feedback for a correct guess

def main():
    user_number_guess(random.randrange(1, 100))                  # Call the function with a random number between 1 and 99

main()                                                           # Start the program

