"""
The program displays the staff members basic information and total requisition.

Author: Rajiv Akaash Deo
"""
def display_requisitions(counter_id):

    #collect user data
    staff_id, staff_name = collect_user_data
    #check payment status
    date, requisition_id, status, approval_reference_number, total_requisition  = check_payment_status
    # Generate the detailed report
    print(f"Printing Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: {total_requisition}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {approval_reference_number}")
    print("------------------------\n")
    # Return updated counter if needed for further use
    return counter_id
display_requisitions(counter_id)


