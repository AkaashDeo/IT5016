"""

TASK 1: `staff_info`

1. **Function Parameters**: The `staff_info` function should not require a `uniqueID` parameter because it 
generates the ID internally.
2. **ID Generation**: Instead of passing a `uniqueID`, you should generate it within the function.

"""
#**Updated Code:**


def staff_info(counter):                                # Function Definition: defines a function named staff_info that takes a single argument, counter.
    date = input("Enter Date: ")                        # Input: prompts the user to enter a date and stores the input in the date variable.
    staffID = input("Enter Staff ID: ")                 # Input: prompts the user to enter a staff ID and stores the input in the staffID variable.
    name = input("Enter Staff Name: ")                  # Input: prompts the user to enter the staff's name and stores it in the name variable.
    
    # Generate Requisition ID
    uniqueID = counter + 10000                          # generates a uniqueID by adding 10000 to the counter value. This provides a way to create a unique identifier based on the counter value.
    print(f"\nPrinting Staff Information:\nDate: {date}\nStaff ID: {staffID}\nStaff Name: {name}\nRequisition ID: {uniqueID}") # prints the collected information along with the generated uniqueID in a formatted string.
    
    return staffID, uniqueID, date, name                # returns a tuple containing the staffID, uniqueID, date, and name values. This allows the function to provide these values to the caller.

# Initialize counter and call function
counter = 1000                                          # staff_info(counter) calls the staff_info function with counter as the argument.
staff_info(counter)                                     # This will prompt the user to enter the date, staff ID, and staff name, then generate and display the requisition ID based on the counter

# Summary
""" The function staff_info collects user input for date, staff ID, and staff name.
It generates a unique requisition ID based on the provided counter value.
It prints the collected information and returns these values as a tuple.
The counter value is used to ensure that each requisition ID is unique by adding a fixed offset (10000) to it."""

"""
 TASK 2: `requisition_total`

1. **Loop Exit**: The loop condition and exit logic need adjustment.
2. **Sum Calculation**: The summation logic should be outside the loop.

"""

# **Updated Code:**

def requisition_total():                          # This line defines a function named requisition_total with no parameters.
    # inside the function
    all_items = []                                # An empty list that will be used to store dictionaries. Each dictionary will represent an item with its name and price.
    total_sum = 0                                 # A variable initialized to 0 that will keep track of the total price of all items.

    while True:                                   # Starts an infinite loop that will continue until explicitly broken.
        item_name = input("\nEnter item name: ")  # Prompts the user to enter the name of an item.
        price = float(input("Enter item price: "))# Prompts the user to enter the price of the item and converts it to a float for numerical operations.
        
        item_object = {item_name: price}          # Creates a dictionary where the item name is the key and the price is the value.
        all_items.append(item_object)             #  Adds the dictionary to the all_items list.
        
        another = input("\nAdd another item? (y/n): ") # Asks the user if they want to add another item.
        if another.lower() != "y":                     # If the user inputs anything other than "y" (case insensitive), the loop breaks, ending the input process.
            break
    
    # Calculate total sum, The nested for loops iterate through the all_items list.
    for item in all_items:                        # Iterates over each dictionary in the all_items list.
        for value in item.values():               # Iterates over the values in the current dictionary (i.e., the item prices).
            total_sum += value                    # Adds each price to total_sum, which accumulates the total cost of all items.
    # Output and Return
    print(f"Total: ${total_sum:.2f}")             #  Prints the total sum formatted to two decimal places, prefixed by a dollar sign.
    return total_sum                              #  Returns the total sum of all item prices from the function. This allows the calling code to use or display the total if needed.

# Summary

"""Summary
Purpose: The function requisition_total collects item names and prices from the user, stores them, calculates the total cost, and prints the total.
Usage: It continuously prompts the user for item details until they choose not to add more items, computes the sum of the item prices, and displays it formatted as currency.
This function is useful for scenarios where you need to aggregate prices for a list of items and display the total amount."""


"""
TASK 3: IMPLEMENT`requisition_approval`

1. **Ref Num Calculation**: Ensure the `ref_num` is always initialized and check conditions properly.
2. **Return Values**: Ensure `ref_num` is always returned even if it's not used.

"""

# **Updated Code:**

def requisition_approval(staffID, uniqueID, total_sum):  # This line defines a function named requisition_approval with three parameters: An identifier for the staff member, An identifier for the requisition, The total amount of the requisition.

    if total_sum < 500:                                  # if total_sum < 500:: Checks if the total sum of the requisition is less than $500.
        status = "Approved"                              # Sets the status to "Approved".
        id_str = str(uniqueID)                           # Converts uniqueID to a string to facilitate string manipulation.

        ref_num = str(staffID) + id_str[-3:]             # Creates the reference number by concatenating staffID (converted to a string) with the last three characters of id_str.
        print(f"\nTotal: ${total_sum:.2f}\nStatus: {status}\nApproval Reference Number: {ref_num}") # Prints the total amount, status, and the approval reference number formatted to two decimal places.
    else:                                                # If total_sum is $500 or more:
        status = "Pending"                               # Sets the status to "Pending".
        ref_num = None                                   # Sets ref_num to None since no reference number is generated for pending requests.
        print(f"\nTotal: ${total_sum:.2f}\nStatus: {status}") # Prints the total amount and status, without a reference number.
    # Return Statement
    return status, ref_num            # The function returns a tuple containing:
                                                                               # status: The approval status ("Approved" or "Pending").
                                                                               # ref_num: The reference number if the status is "Approved", or None if the status is "Pending".


# Summary 
"""
Purpose: The requisition_approval function determines whether a requisition is approved based on its total amount. 
It generates and prints an approval reference number for approved requisitions and sets the status accordingly.
Logic:
If the total amount is less than $500, the requisition is approved, and a reference number is created and printed.
If the total amount is $500 or more, the requisition is marked as pending, and no reference number is generated.
Return: The function returns the status of the requisition and the reference number (or None if pending), 
allowing the calling code to use or display these values as needed."""


"""
TASK 4: `display_requisitions`

1. **Function Calls**: Make sure to call the correct functions and pass necessary parameters.
2. **Correct Function Call**: `requisition_total` should be called with parentheses to execute and return a value.
"""
# Inside the Function
def display_requisitions():                                  # 
    global counter                                           # This statement allows the function to use the global counter variable defined outside the function. It ensures that the function refers to the counter variable declared globally rather than a local one.
    staffID, uniqueID, date, name = staff_info(counter)      # Calls the staff_info function with counter as an argument. This function returns the staffID, uniqueID, date, and name, which are captured in corresponding variables
    total_sum = requisition_total()                          # Calls the requisition_total function, which prompts the user for item details, calculates the total cost, and returns it. The total sum is stored in the total_sum variable.
    status, ref_num = requisition_approval(staffID, uniqueID, total_sum) # Calls the requisition_approval function with the staffID, uniqueID, and total_sum as arguments. This function determines the approval status and generates a reference number if the requisition is approved.
    # Prints the collected and computed information in a formatted manner.
    print(f"\nPrinting Requisition:\nDate: {date}\nRequisition ID: {uniqueID}\nStaff ID: {staffID}\nStaff Name: {name}\nTotal: ${total_sum:.2f}\nStatus: {status}\nApproval Reference Number: {ref_num if ref_num else 'N/A'}\n")

# tASK 4
# Calling the Function
counter = 1000 # Initialize counter: Sets the initial value of the counter variable to 1000.
display_requisitions() # Calls the display_requisitions function to execute the full process, 
                       # including gathering staff information, calculating totals, determining approval status, and printing the requisition details.


""" Summary

Purpose: 

The display_requisitions function consolidates the process of gathering requisition details, 
calculating totals, determining approval status, and displaying all relevant information in a formatted output.
Integration: It uses the staff_info, requisition_total, and requisition_approval functions to collect data and 
process it, ensuring a comprehensive display of the requisition.

Usage: 

The function is useful for handling and displaying the entire requisition approval process in a single 
step, providing a clear overview of the requisition details and its approval status.

"""