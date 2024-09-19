"""
STRING MULTIPLICATION

Author Rajiv Deo

"""
# INPUT
praise = "good!"                                   # praise is the STRING VARIABLE assigned the value "good!"
# PROCESS
lot_of_praise = praise * 4                         # lot_of_praise is created by multiplying the praise STRING by 4, which results in "good!good!good!good!".
#OUTPUT
print (praise)                                     # The print(praise) statement outputs "good!".
print (lot_of_praise)                              # The print(lot_of_praise) statement outputs "good!good!good!good!".

"""
STRING MULTIPLICATION : The code demonstrates string multiplication, a function for converting hours and minutes into total minutes, 
and provides a way to interactively calculate and display the total minutes based on user input.

Author Rajiv Deo

"""
def get_minutes(hours, minutes):                   # get_minutes is a function that converts hours and minutes into total minutes. 
    total = hours * 60 + minutes                   # It multiplies the number of hours by 60 and adds the number of minutes.
    return total
# INPUT
hours = float(input("Enter hours:"))               # The user is prompted to enter hours.
minutes = float(input("Enter minutes:"))           # The user is prompted to enter minutes.
# PROCESS
total_minutes = get_minutes(hours,minutes)         # These values are passed to the get_minutes function, which calculates the total minutes.
# OUTPUT
print(total_minutes,"minutes")   # The result is printed with "minutes".

