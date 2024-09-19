"""
The following code shows how to slice a string in Python.

Author: Rajiv Deo """
# INPUT
greeting ="Hello World"        # greeting is a string variable assigned the value "Hello World".
#PROCESS
first_part = greeting[0:4]     # slices the string greeting from index 0 to 3 (index 4 is not included), Result: "Hell" (the substring starting from index 0 up to but not including index 4).
second_part = greeting[6:10]   # slices the string greeting from index 6 to 9 (index 10 is not included), Result: "Worl" (the substring starting from index 6 up to but not including index 10).
# OUTPUT
print(second_part,first_part)  # prints the values of second_part and first_part, separated by a space, Given the previous results, this prints "Worl Hell".

