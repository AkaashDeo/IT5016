def reverse_string(s):
    """
    Reversing a given string.

    Author: Akaash Deo
    """
    reversed_str = ""                                       # Initialize an empty string to store the reversed result
    for char in s:                                          # Loop through each character in the input string
        reversed_str = char + reversed_str                  # Prepend the character to the reversed string
    return reversed_str                                     # Return the reversed string

def main():
    """
    Main function to execute the string reversal program. It prompts the user for a string,
    calls the reverse_string function, and prints both the original and reversed strings.
    """
    original_string = input("Enter a string: ")             # Prompt user for input
    reversed_string = reverse_string(original_string)       # Call the reverse function
    print(f"Original: {original_string}")                   # Display the original string
    print(f"Reversed: {reversed_string}")                   # Display the reversed string

                                                            # Run the main function
if __name__ == "__main__":                                  # Check if the script is being run directly
    main()                                                  # Execute the main function
