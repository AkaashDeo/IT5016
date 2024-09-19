"""Function with one argument and a return value

Author: Akaash Deo"""

def aFunction(anArg):                          # Define a function named aFunction that takes one argument
    return anArg + 1                          # Return the argument incremented by 1

result = aFunction(5)                          # Call the function with 5 and store the result in the variable result

# Different ways of calling a function with a keyword argument
def aFunction(anArg, optionalArg=1):          # Define a function with a required argument and an optional argument (default value of 1)
    return anArg + optionalArg                 # Return the sum of the required and optional arguments

print(aFunction(5))                            # Call the function with 5, using the default value for optionalArg; print the result
print(aFunction(5, 4))                         # Call the function with 5 and 4; print the result
print(aFunction(5, optionalArg=4))             # Call the function using a keyword argument for optionalArg; print the result
