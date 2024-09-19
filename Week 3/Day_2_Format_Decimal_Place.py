"""
The following function shows how to format decimal places.

Author: Akaash Deo
"""

pi = 3.141592653589                                          # Assign the value of Pi.
print(pi)                                                    # Print the original value of Pi.

"""Format Pi to 2 decimal places using f-string"""

formatted_pi = f"Value of Pi to 2 decimal places: {pi:.2f}"
print(formatted_pi)                                          # Print the formatted value of Pi.

salary = float(input("Enter your weekly salary: "))          # Prompt the user for their weekly salary.
print(f"Your weekly salary is ${salary:.2f}")                # Print the salary formatted to 2 decimal places.
