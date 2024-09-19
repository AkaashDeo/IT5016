"""
String Concatenation Program

This program prompts the user to enter two strings, a staff ID, and a requisition ID. 
It then concatenates the strings and the IDs, displaying the results in a formatted manner.

Author: Akaash Deo
"""
s1 = input('Please enter the first string:\n')                                           # Prompt for the first string
s2 = input('Please enter the second string:\n')                                          # Prompt for the second string

# Print the concatenated string
print('Approval', 'Concatenated String =', s1 + s2)                                      # Output the concatenated string

# Since staff_id and requisition_id are defined earlier in the code
staff_id = input('Please enter the staff ID:\n')                                         # Prompt for staff ID
requisition_id = input('Please enter the requisition ID:\n')                             # Prompt for requisition ID

# Print the approval reference number
print("Approval Reference Number:", "Concatenated String =", staff_id + requisition_id)  # Output the concatenated IDs
