"""

Lists in Detail explained.

Author: Akaash Deo"""


aList = [1, 2, 3, 4]                        # Initialize a list with four integer elements
type(aList)                                 # Get the type of aList
# output: list                               # The type of aList is a list

# Append item to a list
aList.append(5)                             # Add the integer 5 to the end of aList
aList                                       # Display the current contents of aList
# output: [1, 2, 3, 4, 5]                   # aList now contains five elements

# List concatenation
[1, 2, 3] + [4, 5, 6]                      # Concatenate two lists
# output: [1, 2, 3, 4, 5, 6]                # Resulting list from concatenation

# List multiplication
[1, 2] * 5                                  # Multiply the list [1, 2] by 5
# output: [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]    # Resulting list repeats [1, 2] five times

# Accessing items in a list
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # Initialize a new list with ten integer elements

# Print the item at index 4
print(aList[4])                             # Access the element at index 4 (5th element)
# output: 5                                  # The item at index 4 is 5

# Print the items at index 0, up to (not including) index 4
print(aList[0:4])                           # Slice the list from index 0 to 3 (4 is excluded)
# output: [1, 2, 3, 4]                       # Prints the first four elements

# If the first index is missing, it's assumed to be 0
print(aList[:4])                            # Slice the list from the start up to index 4
# output: [1, 2, 3, 4]                       # Same result as above

# If the last index is missing, it's assumed to go to the end of the list
print(aList[4:])                            # Slice the list starting from index 4 to the end
# output: [5, 6, 7, 8, 9, 10]                # Prints elements from index 4 to the end

# Print every other item in the list
print(aList[::2])                           # Slice the list to get every second element
# output: [1, 3, 5, 7, 9]                    # Prints items at even indices

# Print every third item in the list
print(aList[::3])                           # Slice the list to get every third element
# output: [1, 4, 7, 10]                      # Prints items at indices 0, 3, 6, and 9
