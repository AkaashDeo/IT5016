"""
Generate a unique ID and collect staff information.

Author: Akaash Deo

"""

def staff_info(counter):

    # Prompt the user for details
    date = input("Enter Date: ")                # Collect the date from the user.
    staffID = input("Enter Staff ID: ")         # Collect the staff ID from the user.
    name = input("Enter Staff Name: ")          # Collect the staff name from the user.

    # Generate unique ID by adding 10000 to the counter
    uniqueID = counter + 1000034                # Create a unique requisition ID.

    return staffID, uniqueID, date, name        # Return the collected information as a tuple.

# Initialize counter and call the function
counter = 1000                                  # Set the initial value for the counter.
staff_info(counter)                             # Call the staff_info function to collect staff information.
