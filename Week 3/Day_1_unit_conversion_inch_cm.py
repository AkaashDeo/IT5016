"""
This program contains two functions: one to convert inches to centimeters 
and another to convert centimeters to inches.

Author: Akaash Deo
"""

def inches_to_cm(inches):                                    # Define a function that takes inches as a parameter.
    "Convert inches into centimeters"                        # A brief description of what the function does.
    cm = inches * 2.54                                       # Calculate centimeters using the conversion factor.
    return cm                                                # Return the converted value in centimeters.

# INPUT
inches = int(input("Enter value to convert from inches: "))  # Prompt user for input in inches.
# PROCESS
cm = inches_to_cm(inches)                                    # Call the conversion function and store the result.
# OUTPUT
print(cm, "cm")                                              # Print the converted value in centimeters.

def cm_to_inches(cm):                                        # Define a function that takes centimeters as a parameter.
    "Convert centimeters to inches"                          # A brief description of what the function does.
    inches = cm / 2.54                                       # Calculate inches using the conversion factor.
    return inches                                            # Return the converted value in inches.

# INPUT
cm = int(input("Enter value to convert from cm: "))          # Prompt user for input in centimeters.
# PROCESS
inches = cm_to_inches(cm)                                    # Call the conversion function and store the result.
# OUTPUT
print(inches, "inches")                                      # Print the converted value in inches.
