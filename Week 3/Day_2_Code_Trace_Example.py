"""
The following shows how to code trace.

Author: Akaash Deo
"""

def main():                                       # Define the main function.
    a = 42                                        # Initialize variable a with value 42.
    b = 17                                        # Initialize variable b with value 17.
    c = 94                                        # Initialize variable c with value 94.

    if a > b and a > c:                           # Check if a is greater than both b and c.
        print("you")                              # Print "you" if the condition is true.

    if not (a > b and a > c):                     # Check if a is not greater than both b and c.
        print("cannot")                           # Print "cannot" if the condition is true.

    if a > b or a > c:                            # Check if a is greater than either b or c.
        print("tuna")                             # Print "tuna" if the condition is true.

    if not (a > b or a > c):                      # Check if a is not greater than either b or c.
        print("fish")                             # Print "fish" if the condition is true.

# No output yet as we have not called the main function yet.

main()                                            # Call the main function to execute the code.
