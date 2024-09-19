"""
This program demonstrates basic operations on lists and tuples.
Author: Rajiv Deo
"""

"""Append an item to the list"""
animals = ['lion', 'elephant', 'tiger', 'giraffe']
animals.append('zebra')                                # Adding 'zebra' to the list
print(animals)                                         # Output the updated list

"""Remove an item from the list"""
animals.remove('tiger')                                # Removing 'tiger' from the list
print(animals)                                         # Output the updated list

"""Tuples"""
tuple1 = (3, 6, 8)                                     # Creating a tuple
print(tuple1)                                          # Output the tuple
print()                                                # Just gives a new line of space in output!

tuple2 = ("abcde", "ghij", "klmno")                    # Creating another tuple
print(tuple2)                                          # Output the second tuple
