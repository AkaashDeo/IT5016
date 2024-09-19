"""
The following function shows how to utilize multi-line F strings.

Author: Akaash Deo
"""

name = "James"                                    # Assign the name.
age = 28                                          # Assign the age.
address = "121 Queen Street"                      # Assign the address.

"""Create a multi-line F string to format the information"""

info = f"""
Name: {name}
Age: {age}
Address: {address}
"""
print(info)                                       # Print the formatted information.
