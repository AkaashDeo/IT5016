"""
Demonstration of various mathematical and data manipulation functions in Python.

- Find the Absolute Value of a Complex Number
- Take the Minimum and Maximum from Two Numbers
- Rounding FLOAT to nearest INTEGER
- POWER Function
- Sort a TUPLE in REVERSE ORDER
- Sum of elements in a TUPLE

Author: Rajiv Deo
"""

""" Find the Absolute Value of a Complex Number """
# INPUT
a = 3+5j                                      # a is a complex number with a real part of 3 and an imaginary part of 5.
# PROCESS & OUTPUT
print(abs(a))                                 #  computes the absolute value (or magnitude) of the complex number. For a complex number 

""" Take the Minimum and Maximum from Two Numbers """
# INPUT
x = 200
y = 20
# PROCESS & OUTPUT
print(min(x,y))                               # returns the smaller of the two values, x and y.
print(max(x,y))                               # returns the larger of the two values, x and y.

""" Rounding FLOAT to nearest INTEGER """
# INPUT
x = 200.34
y = 20.87
# PROCESS & OUTPUT
print(round(y))                               # Rounds the floating-point number y to the nearest integer. Result: 21 (since 20.87 rounded to the nearest whole number is 21).

""" Power Function """
print(pow(2,3))                               # pow(2, 3) calculates 2 raised to the power of 3, result: 8

""" Sort a TUPLE in REVERSE ORDER """
# INPUT
a = ('Hello', 'Pinal', 'Apple', 'zebra') 
# PROCESS
result = sorted(a,reverse=True)               # sorts the tuple a in reverse (descending) order.
# OUTPUT
print(result)                                 # Result: ['zebra', 'Pinal', 'Hello', 'Apple'] (sorted in reverse alphabetical order).

""" Sum of elements in a TUPLE """
# INPUT
b = (10, 20, 30, 40, 50) 
# PROCESS
r1 = sum(b)                                   # calculates the sum of all elements in the tuple b.
# OUTPUT
print(r1)                                     # Result: 150 (the sum of 10, 20, 30, 40, and 50).