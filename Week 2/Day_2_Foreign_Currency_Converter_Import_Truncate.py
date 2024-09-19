""" 
Currency Conversion and Truncation Program

This program performs currency conversions between New Zealand Dollars 
(NZD) and Australian Dollars (AUD) based on a given exchange rate. 
It also demonstrates the truncation of a currency value to an integer.

Author: Akaash Deo
"""

# INPUT
amount_to_convert = 500                                   # Convert $500 NZD to Australian dollars and vice versa, and truncate the NZD value. Define the amount to convert
nz_to_aus_rate = 0.95                                     # Define the exchange rate from NZD to AUD
# PROCESS
"""Conversion from NZD to AUD"""
nz_dollars = amount_to_convert                            # Set the amount in NZD
aus_dollars = nz_dollars * nz_to_aus_rate                 # Calculate the equivalent amount in AUD
"""Conversion from AUD to NZD"""
aus_dollars = amount_to_convert                           # Set the amount in AUD
nz_dollars = aus_dollars / nz_to_aus_rate                 # Calculate the equivalent amount in NZD
"""Import Function"""
import math                                               # Import the math module to use the trunc() function
num1 = math.trunc(nz_dollars)                             # Truncate the NZD amount to get the integer part
# OUTPUT
print("NZ $", nz_dollars, "= AUS $", aus_dollars, sep="") # Output the conversion result from NZD to AUD
print("AUS $", aus_dollars, "= NZ $", nz_dollars, sep="") # Output the conversion result from AUD to NZD
print(num1)                                               # Output the truncated NZD value
