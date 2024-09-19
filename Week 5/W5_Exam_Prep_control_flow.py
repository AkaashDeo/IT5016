#CONTROL FLOW

# IF/ELSE STATEMENTS
#Example1
a = False
if a:
    print("It is true!")
    print("Also print this.")
else:
    print("It is false")

print("Always print this.")

#Example2
a = True
b = True
c = False

if a:
    print("The statement is true for a")
    if b:
        print("The statement is true again for b")
        if c:
            print("The statement is false for 3")
else:
    print("Statement is neither true or false.")

a = False

if a:
    print("The statement is true")
else:
    print("Statment is false")

# FOR Loops: avoids excessive indenting, iteriable
a = [1,2,3,4,5]
for item in a:
    print(item)



# WHILE LOOPS: doesnt iteriate, it just looping until boolean you passed is false.

a = 0
while a < 5:
    print(a)
    a = a + 1
    # its very important to have above otherwise loop will not divert and will be printing zero forever.





