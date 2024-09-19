"""
Exam Prep: Data Structures

Author: Akaash Deo
"""

# Lists

#list of integers
my_list = [1,2,3,4,5,6]
print(my_list)

#list of strings
my_list = ["list","of","strings"]
print(my_list)

# mixed list
my_list = ["rescue", 1, 2, True, False]
print (my_list)

print(len(my_list))

#Sets: similar to lists except FOR ALL ELEMENTS NEED TO BE UNIQUE

my_set = {1,1,1,1,1,2,3,4,5}
print(my_set)

# Tuples: can't append or add things?? they're memory efficient, python knows you cant add to them so it only keeps the amount of memory needed to store tuples.
# Good for storing little things like x,y cordinates

my_tuple = (1,2,3,4,5,6)
print (my_tuple)

# Dictionary

my_dictionary = {
    "apple" : "A red fruit",
    "bear" : "A scary animal"
}
my_dictionary ["apple"]
print(my_dictionary)