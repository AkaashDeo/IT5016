"""
This program defines a function that converts degrees Celsius to degrees Fahrenheit.
It uses the formula: Fahrenheit = (Celsius * 9/5) + 32.

Author: Akaash Deo
"""

def celsius_to_f(celsius):                                             # Define the function that takes Celsius as input.
    fahrenheit = (celsius * 9/5) + 32                                  # Convert Celsius to Fahrenheit using the formula.
    return fahrenheit                                                  # Return the calculated Fahrenheit value.

# INPUT
celsius = 34                                                           # Set the Celsius value to convert.
# PROCESS
current_celcius = celsius_to_f(celsius)                                # Call the function to convert Celsius to Fahrenheit.
# OUTPUT
print(celsius)                                                         # Print the original Celsius value.
print(celsius, "degrees Celsius", "=", current_celcius, "Fahrenheit")  # Print the conversion result.
