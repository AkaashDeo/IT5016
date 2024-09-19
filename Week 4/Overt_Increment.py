"""
When we don't need an overt increment statement.

Author: Rajiv Deo
"""

def total_user_numbers():
    """
    This function prompts the user to enter numbers, summing them up until the user enters 0.
    """
    total = 0                                                       # Initialization
    while True:
        try:
            number = int(input("Enter a number (0 to end): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if number == 0:
            break                                                    # Exit the loop if the number is 0

        total += number                                              # Accumulate the total

    print("Total:", total)                                           # Print the total

def main():
    total_user_numbers()

if __name__ == "__main__":
    main()
