"""
The code initializes `counter` and repeatedly checks conditions within a `while` loop.
 It prints messages based on the value of `count` and adjusts `counter` accordingly. 
 The loop eventually exits when `counter` reaches `5`.
 
 Author: Rajiv Deo"""


counter = 1                       # Purpose: Initializes the variable `counter` with the value `1`. 
                                  # This will be used to control the loop and make comparisons inside the loop.

while (counter < 5):              # Purpose: Starts a `while` loop that will continue to execute as long as the condition `counter < 5` is `True`.
                                  #`while`: A control flow statement that repeatedly executes a block of code as long as a condition is `True`.
                                  # `counter < 5`: The loop continues executing as long as `counter` is less than `5`.
    count = counter               # Purpose: Assigns the current value of `counter` to the variable `count`. 
                                  # This creates a local variable `count` that holds the same value as `counter` for this iteration of the loop.

    if count < 2:                 # Purpose: Checks if the value of `count` is less than `2`.
                                  # `if`: A conditional statement that executes the following block of code if the condition is `True`.
        counter = counter + 1     # Purpose: Increments the value of `counter` by `1` if the condition `count < 2` is `True`. 
                                  # This is to ensure that `counter` eventually reaches `5` and the loop terminates.

    else:                         # 'else'-> Purpose: Specifies the block of code to be executed if the `if` condition (`count < 2`) is not `True`.
        print('Less than 2')      # `print('Less than 2')`
                                  # Purpose: Prints the string `'Less than 2'` to the console if `count` is not less than `2` (i.e., `count` is `2` or more).

    if count > 4:                 # Purpose: Checks if the value of `count` is greater than `4`.
                                  # `if`: Another conditional statement inside the loop.
        counter = counter + 1     # Purpose: Increments the value of `counter` by `1` if the condition `count > 4` is `True`. 
                                  # This ensures `counter` is adjusted if `count` is greater than `4`.
    else:                         # `else:` -> Purpose: Specifies the block of code to be executed if the `if` condition (`count > 4`) is not `True`.

        print('Greater than 4')   # Purpose: Prints the string `'Greater than 4'` to the console if `count` is not greater than `4` (i.e., `count` is `4` or less).
    counter = counter + 1         # `counter = counter + 1` -> Purpose: Increments the value of `counter` by `1` at the end of each iteration of the loop. 
                                  # This ensures that `counter` progresses towards the loop termination condition (`counter < 5`).


""" 
Loop Execution Walkthrough

1. First Iteration:
   - `counter` starts at `1`.
   - `count` is assigned the value `1`.
   - `if count < 2`: `True`, so `counter` becomes `2`.
   - `if count > 4`: `False`, so `print('Greater than 4')` executes.
   - At the end of the loop, `counter` is incremented to `3`.

2. Second Iteration:
   - `counter` is `3`.
   - `count` is `3`.
   - `if count < 2`: `False`, so `print('Less than 2')` executes.
   - `if count > 4`: `False`, so `print('Greater than 4')` executes.
   - At the end of the loop, `counter` is incremented to `4`.

3. Third Iteration:
   - `counter` is `4`.
   - `count` is `4`.
   - `if count < 2`: `False`, so `print('Less than 2')` executes.
   - `if count > 4`: `False`, so `print('Greater than 4')` executes.
   - At the end of the loop, `counter` is incremented to `5`.

4. Loop Termination:
   - Now `counter` is `5`, which does not satisfy `counter < 5`, so the loop terminates.

"""