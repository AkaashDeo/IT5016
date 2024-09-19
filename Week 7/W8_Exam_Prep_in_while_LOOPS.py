""" if / else Explained.

Author: Akaash Deo"""

if False:                                     # Check if the condition is False
    print('This does not print')              # This block won't execute
else:                                         # If the condition is False, execute this block
    print('This will print')                  # This line will execute

if True:                                      # Check if the condition is True
    print('This does not print')              # This block will execute
else:                                         # If the condition is True, this block will not execute
    print('This will print')                  # This line won't execute

# Iterate through items in a range
for i in range(0, 5):                        # Loop through numbers from 0 to 4
    print('Number: {}'.format(i))            # Print the current number in the loop

# Iterate through items in a list
for i in [1, 2, 3, 4, 5]:                    # Loop through each item in the list
    print('Number: {}'.format(i))            # Print the current item in the list

i = 0                                         # Initialize i to 0
while i < 5:                                  # Continue looping while i is less than 5
    print('Number: {}'.format(i))            # Print the current value of i
    i = i + 1                                 # Increment i by 1
