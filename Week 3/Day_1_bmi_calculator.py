"""
This program calculates the Body Mass Index (BMI) using a function that takes weight and height as inputs.

Author: Akaash Deo
"""

def get_bmi(weight, height):                      # Define a function that takes weight and height as parameters.
    total = weight / (height / 100) ** 2          # Calculate BMI using the formula: weight / (height in meters)^2.
    return total                                  # Return the calculated BMI value.

# INPUT
weight = int(input("Enter weight (in kg): "))     # Prompt user for their weight in kilograms.
height = int(input("Enter height (in cm): "))     # Prompt user for their height in centimeters.
# PROCESS
total = get_bmi(weight, height)                   # Call the function to calculate BMI and store the result.
# OUTPUT
print(total, "BMI is")                            # Print the calculated BMI value.
