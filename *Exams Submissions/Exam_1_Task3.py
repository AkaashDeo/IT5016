
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

def requisitions_total():
    total_requisition = 0 #Initialize the total to 0

    print("\nEnter each requisition details (Item Name, Item Price). Type 'finish' when you are done.\n")

    while True:
        # Prompt the user to enter the item amount or "finish" to stop
        user_input = input("Enter Name and Price (E.g. Cables $200.00): ")

        if user_input.lower() =="finish":
            break

        try:
            # Convert the input to a float and add to the total amount
            price = float(user_input)
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            total_requisition += price
        except ValueError:
            # Handle invalid input that cannot be converted to a float
            print("Invalid input. Please enter a valid number or 'finish' to end.")
    
    # Print the total amount
    print(f"${total_requisition:.0f}")

requisitions_total()





"""
The program carries on from tasks 1,2 and is intended to make approval decisions for the requisition requests being made.

Author: Rajiv Akaash Deo
"""


def requisition_approval():
    # Determine the status based on the total amount
    if total_requisition < 500:
        status = "Approved."
    else: 
        status = "Pending."
        
    # Print the status and Approval Reference number.
    print(f"{total_requisition}")
    print(f"Status: {status}")
    print("Approval Reference Number: ", "Concatenated String =", staff_id + requisition_id)
    return
requisition_approval()
   
