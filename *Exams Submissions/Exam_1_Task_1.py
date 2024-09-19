
"""
The program collects information about staff members who submit requisitions in the company.

Upon submission, a unique id is created.

Author: Rajiv Akaash Deo

"""

def staff_info(counter_id):               # Parameters: counter_id (int): The current counter ID to generate a new unique requisition ID.

    # Prompt staff member for input
    date = input("\nDate: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")
    # Generate a unique ID by adding 1 to the current counter value
    requisition_id = counter_id + 1
    # Print the user information in a formatted manner
    print(f"\nPrinting Staff Information: ")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition ID: {requisition_id}") 
    # Return updated counter_id and the collected information
    return requisition_id, date, staff_id, staff_name
# Example usage
staff_info(10000)

