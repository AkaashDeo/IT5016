"""
This program demonstrates various string methods in Python.

1. Check if a string contains only alphabetic characters.
2. Check if a string contains only digits.
3. Check if a string contains alphanumeric characters.
4. Find the first occurrence of a substring.
5. Find the last occurrence of a substring.
6. Count the frequency of a substring.

Author: Akaash Deo
"""

""" 1. Check if String Contains Only Alphabetic Characters """
student_id = "20241400"                      # Initialize the string variable 'student_id' with a numeric ID.
print(student_id.isalpha())                  # The isalpha() method checks if all characters in 'student_id' are alphabetic.
                                             # Result: False, since "20241400" contains digits, not just alphabetic characters.

""" 2. Check if String Contains Only Digits """
print(student_id.isdigit())                  # The isdigit() method checks if all characters in 'student_id' are digits.
                                             # Result: True, because "20241400" consists entirely of digits.

""" 3. Check if String Contains Alphanumeric Characters """          
print(student_id.isalnum())                  # The isalnum() method checks if all characters in 'student_id' are either alphabetic or numeric.
                                             # Result: True, as "20241400" is composed solely of numeric characters.

""" 4. Find the First Occurrence of a Substring """
txt = "find me if you can"                   # Initialize the string variable 'txt' with a sample sentence.
print(txt.find('i'))                         # The find() method returns the index of the first occurrence of the substring 'i' in 'txt'.
                                             # Result: 8, as the first 'i' appears at index 8 in the string "find me if you can".

""" 5. Find the Last Occurrence of a Substring """
print(txt.rfind('i'))                         # The rfind() method returns the index of the last occurrence of the substring 'i' in 'txt'.
                                             # Result: 11, as the last 'i' appears at index 11 in the string "find me if you can".

""" 6. Count the Frequency of a Substring """    
print("Frequency of 'i' is:", txt.count('i')) # The count() method returns the number of times the substring 'i' appears in 'txt'.
                                             # Result: 2, as 'i' appears twice in "find me if you can".
