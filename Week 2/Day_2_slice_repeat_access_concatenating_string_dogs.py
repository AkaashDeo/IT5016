"""
Demonstration of string manipulation techniques in Python.

1. Slicing and Printing a Substring
2. Repeating a Substring
3. Accessing a Specific Character from the End
4. Concatenating Two Characters
5. Slicing the String from the End

Author: Rajiv Deo 
"""
# INPUT
s = "dogs have masters. Cats have staff."                 # s is a string variable assigned the value "dogs have masters. Cats have staff.".
# PROCESS AND OUTPUTS
""" 1. Slicing a Substring """

print("1.", s[1:6])                                       # s[1:6] slices the string s from index 1 to 5 (index 6 is not included), Result: "ogs h" (substring starting from index 1 up to but not including index 6).

""" 2. Repeating a Substring """

print("2.", s[:2] * 3)                                    # s[:2] slices the string s from the start up to but not including index 2. s[:2] evaluates to "do", # s[:2] * 3 repeats "do" three times. Result: "dododo" (the substring "do" repeated three times).

""" 3. Accessing a Specific Character from the End """

print("3.", s[-3])                                        # s[-3] accesses the third-to-last character of the string s, Result: "s" (the character at index -3, which is the third character from the end).

""" 4. Concatenating Two Characters """

print("4.", s[4] + s[1])                                  # s[4] accesses the character at index 4, s[1] accesses the character at index 1, s[4] is "s" and s[1] is "o", # s[4] + s[1] concatenates these two characters. Result: "so" (the characters at index 4 and index 1 combined).








""" 5. Slicing the String from the End """

print("5.", s[-4:])

# s[-4:] slices the string s from the fourth-to-last character to the end.
# Result: "aff." (the substring starting from index -4 up to the end of the string).



