"""
TASK 1:

Create a Python function called staff_info.

Use Python input methods to collect information about a staff member submitting a requisition (i.e., Date, Staff ID, Staff Name, and Requisition ID).

A Unique ID should be generated using a counter plus 10000 and assigned as the requisition ID, as shown in the sample below.

This function should return all inputs and the requisition ID.

Author: Rajiv Deo
"""

def staff_info(uniqueID):                                # Function to collect staff information
    date = input("Enter Date: ")                        # Prompt user to enter the date
    staffID = input("Enter Staff ID: ")                 # Prompt user to enter the staff ID
    name = input("Enter Staff Name: ")                  # Prompt user to enter the staff name

    print(f"\nPrinting Staff Information:\nDate: {date}\nStaff ID: {staffID}\nStaff Name: {name}\nRequisition ID: {uniqueID}")  # Print collected information

    return staffID, uniqueID, date, name                # Return staff ID, unique ID, date, and name

staff_info(1000)                                        # Call the function with an example unique ID


"""
TASK 2:

Create a Python function called requisition_total. 

Call the function staff_info from TASK 1 and then ask the staff to input his requisition items (i.e., each item name with item price).

This function should return the computed value for all the requisition items.
"""

def requisition_total():                                 # Function to compute the total requisition value
    all_items = []                                       # List to hold all item dictionaries
    sum = 0                                             # Variable to keep track of total price
    status = True                                        # Loop control variable

    while status:                                       # Loop to collect item names and prices
        item_name = input("\nEnter item name: ")       # Prompt user for item name
        price = float(input("Enter item price: "))     # Prompt user for item price

        item_object = ({ item_name: price })            # Create dictionary object for the item
        all_items.append(item_object)                   # Add dictionary object to the list

        another = input("\nAdd another item? (y/n): ")  # Ask if the user wants to add another item
        if another.lower() == "y":                      # Check if the response is 'y'
            continue                                     # Continue to next iteration
        else:                                           # If not 'y', process the items
            for item in all_items:                      # Iterate over each item in the list
                for key, value in item.items():        # Iterate over the key-value pairs in the dictionary
                    sum += value                         # Accumulate the total price
            status = False                               # Exit the loop

            print(f"${sum}")                            # Print the computed total

    return sum                                         # Return the total price

"""
TASK 3:

This function is built on TASK 1 & 2. 

Write a Python function called requisition_approval.

This function is intended to make approval decisions based on the conditions provided in the 'Responding to requests' section below.

Responding to requests: 

    The default status of all submitted requisitions should be set as "Pending".
    Once a requisition is approved, the status should change to "Approved".

    If the total of a submitted requisition is less than $500, the system should automatically approve the requisition
    and assign an approval reference number based on the following rule.

        Staff ID followed by the last three characters of the Requisition ID.

        If the Total of a submitted requisition is $500 or higher, the program should automatically set the status to "Pending".
"""

def requisition_approval(staffID, uniqueID, sum):        # Function to decide approval status based on total sum
    if sum < 500:                                       # Check if total is less than $500
        status = "Approved"                             # Set status to Approved
        id_str = str(uniqueID)                          # Convert unique ID to string for reference number
        ref_num = str(staffID) + id_str[-3:]          # Create approval reference number
        print(f"\nTotal: {sum}\nStatus: {status}\nApproval Reference Number: {ref_num}")  # Print approval details
    else:                                               # If total is $500 or higher
        status = "Pending..."                           # Set status to Pending
        print(f"\nTotal: {sum}\nStatus: {status}")    # Print pending status

    return status, ref_num                             # Return status and reference number


"""
TASK 4:

Create a Python function called display_requisitions. 

The function should display the staff's basic information and the total of his requisition.
"""

def display_requisitions():                             # Function to display requisition details
    staffID, uniqueID, date, name = staff_info(1000)  # Collect staff information
    sum = requisition_total()                           # Call requisition_total to compute the total
    status, ref_num = requisition_approval(staffID, uniqueID, sum)  # Determine approval status

    print(f"\nPrinting Requisition:\nDate: {date}\nRequisition ID: {uniqueID}\nStaff ID: {staffID}\nStaff Name: {name}\nTotal: {sum}\nStatus: {status}\nApproval Reference Number: {ref_num}\n")  # Print all requisition details

display_requisitions()                                  # Call the function to execute the program
