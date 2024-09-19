"""
The following is exercise 2 from the week2_Day1 slides.

$1 NZD = $0.95 AUD
Write a program which converts $500 NZD to Australian dollars and converts $500 AUD to NZD using the above exchange rate.
The output of the program should be:
NZ $500 = AUD $475.0
AUD $500 = NZD $526.3157894736842

Author: Rajiv Akaash Deo
"""

# INPUT
nzd_to_aud_rate = 0.95                                                         # Exchange rate from NZD to AUD
amount_to_convert = 500                                                        # Amount to convert in both currencies
# PROCESS
total_aud = amount_to_convert * nzd_to_aud_rate                                # Convert 500 NZD to AUD using the exchange rate
total_nzd = amount_to_convert / nzd_to_aud_rate                                # Convert 500 AUD to NZD by dividing the amount by the exchange rate
# OUTPUT
print("NZ $", amount_to_convert, " = AUD $", format(total_aud, ".1f"), sep="") # Print the conversion result from NZD to AUD
print("AUD $", amount_to_convert, " = NZD $", total_nzd, sep="")               # Print the conversion result from AUD to NZD
