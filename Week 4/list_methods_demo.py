"""
Demonstrating list methods: remove, insert, index access, assignment, append, pop, sort, and reverse.

Author: Akaash Deo
"""

"""Remove method"""
my_list = [1, 2, 3, 'apple', 'lemon']
my_list.remove(2)                          # Remove the element 2 from the list
print(my_list)                             # Output: [1, 3, 'apple', 'lemon']

"""Insert method: you can specify where to insert unlike append which adds to the back"""
my_list = [1, 2, 3, 'apple', 'lemon']
my_list.insert(1, 20)                      # Insert 20 at index 1
print(my_list)                             # Output: [1, 20, 2, 3, 'apple', 'lemon']
print()

"""Accessing the first element"""
my_list = [1, 2, 3, 'apple', 'lemon']
first_element = my_list[3]                 # Accessing the fourth element
print(first_element)                       # Output: 'apple'

"""Changing an element"""
my_list[2] = "watermelon"                  # Change the third element to 'watermelon'
print(my_list)                             # Output: [1, 2, 'watermelon', 'apple', 'lemon']

"""Append: adding 6 to the list"""
my_list = [1, 2, 3, 'apple', 'lemon']
my_list.append(6)                          # Add 6 to the end of the list
print(my_list)                             # Output: [1, 2, 3, 'apple', 'lemon', 6]

"""Pop: removes an element at a specific position or the last element by default"""
popped_element = my_list.pop()             # Remove the last element
print(my_list)                             # Output: [1, 2, 3, 'apple', 'lemon']
print()

"""Sort the list"""
my_list.sort(key=str)                      # Sort the list, converting all items to strings for comparison
print(my_list)                             # Output will be sorted based on string values
print()

"""Reverse the list"""
my_list.reverse()  # Reverse the order of the list
print(my_list)  # Output: [last item, ..., first item]
