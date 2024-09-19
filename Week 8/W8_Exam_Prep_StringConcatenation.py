"""

String concatenation is the process of joining two or more strings together. 
In Python, this is commonly done using the + operator, as seen in the code example.

Here's a quick overview of the components involved:

String Conversion: str(staffID) converts staffID to a string if it's not already one.
Slicing: id_str[-3:] retrieves a substring consisting of the last three characters of id_str.
Concatenation: The + operator combines these two strings into a single string.
This process can be used in various scenarios where you need to create a new string by 
combining existing strings or parts of strings.
"""

# Sample values for staffID and id_str
staffID = 12345
id_str = "abcdefg"

# Convert staffID to a string and get the last 3 characters of id_str
ref_num = str(staffID) + id_str[-3:]

# Output the result
print(ref_num)  # Output will be: '12345efg'

"""

Explanation of the Code:

Variable Initialization:

staffID is set to 12345.
id_str is set to "abcdefg".

String Conversion and Slicing:

str(staffID) converts 12345 to the string "12345".
id_str[-3:] slices the last three characters from "abcdefg", resulting in "efg".

Concatenation:

The + operator combines "12345" and "efg" into "12345efg".

Output:

print(ref_num) prints the resulting concatenated string "12345efg".

You can replace the values of staffID and id_str with any other appropriate values to see how the concatenation 
behaves with different inputs."""