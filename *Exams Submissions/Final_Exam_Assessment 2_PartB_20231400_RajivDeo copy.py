
"""
The program displays the staff members' basic information and total requisition.

Author: Rajiv Akaash Deo
"""

class RequisitionSystem:
    unique_id_counter = 1000                                                # Initialize a global unique ID counter.

    def __init__(self):
        # Initializes the Requisition System with an empty request list.
        self.requests = []                                                  # Initialize an empty list to store all request objects

    def staff_info(self):
        # Collect user details from input
        date = input("Enter the date: ")
        staffID = input("Enter your Staff ID: ")
        name = input("Enter your name: ")
        
        return date, staffID, name                                          # Return collected information

    def requisition_details(self):
        # Collects item details and calculates the total amount.
        items = []                                                          # List to store items and their costs
        total_amount = 0.0                                                  # Initialize total cost

        while True:
            # Collect item details from input
            item_name = input("Enter item name: ")
            item_cost = float(input("Enter item cost: "))                   # Ensure valid input for cost
            items.append((item_name, item_cost))                            # Append item details to list
            total_amount += item_cost                                       # Update total amount

            # Check if user wants to add more items
            more_items = input("Add another item? (y/n): ")
            if more_items.lower() != 'y':                                   # Exit loop if no more items
                break

        return total_amount, items                                          # Return total amount and list of items

    def requisition_approval(self, total_amount):                           # Decides if the request is approved based on the total amount.
        # Approve request if total amount is less than $500
        if total_amount < 500:
            return "Approved"
        else:
            return "Pending"                                                 # Otherwise, set status to "Pending"

    def respond_requisition(self, request_id, approval_status):
        # Allows a manager to respond to a pending request,  Iterate over requests to find the one with the matching ID
        for req in self.requests:
            if req['unique_id'] == request_id:
                # Check if the request status is "Pending" before updating
                if req['status'] == "Pending":
                    req['status'] = approval_status                          # Update the request status
                    print(f"Request ID {request_id} has been updated to {approval_status}.")
                else:
                    print(f"Request ID {request_id} is already {req['status']}.")
                return
        # Handle case where the request ID is not found
        print(f"Request ID {request_id} not found.")

    def display_requisitions(self):
        # Prints information for all request objects.
        # Iterate over all requests to display details
        for req in self.requests:
            print(f"Date: {req['date']}")
            print(f"Requisition ID: {req['unique_id']}")
            print(f"Staff ID: {req['staffID']}")
            print(f"Staff Name: {req['name']}")
            print(f"Total Amount: ${req['total_amount']:.2f}")
            print(f"Status: {req['status']}")
            print(f"Items: {req['items']}")
            print("-" * 40)                                                   # Separator for readability

    def requisition_statistic(self):
        # Displays statistical information about the requisitions.
        # Calculate statistics based on request statuses
        total_requests = len(self.requests)
        approved_requests = sum(1 for req in self.requests if req['status'] == "Approved")
        pending_requests = sum(1 for req in self.requests if req['status'] == "Pending")
        not_approved_requests = sum(1 for req in self.requests if req['status'] == "Not Approved")
        # Display statistics
        print(f"Total number of requests: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")
        print(f"Total number of pending requests: {pending_requests}")
        print(f"Total number of not approved requests: {not_approved_requests}")

    def create_request(self):
        # Creates a new request and adds it to the list.
        # Collect user info and request details
        date, staffID, name = self.staff_info()                                # Get staff information
        total_amount, items = self.requisition_details()                       # Get requisition details
        status = self.requisition_approval(total_amount)                       # Get the approval status

        # Generate a unique ID for the request
        unique_id = RequisitionSystem.unique_id_counter
        RequisitionSystem.unique_id_counter += 1                               # Increment the unique ID counter

        # Create a new request object
        request = {
            'unique_id': unique_id,
            'date': date,
            'staffID': staffID,
            'name': name,
            'total_amount': total_amount,
            'items': items,
            'status': status
        }

        # Add the request to the list
        self.requests.append(request)                                           # Store the new request
        print(f"Request created with ID: {unique_id}")                          # Confirm request creation


# Example:
if __name__ == "__main__":
    system = RequisitionSystem()                                                # Create an instance of RequisitionSystem
    # Create a new request
    system.create_request()                                                     # Call to create a new request
    # Display all requests
    system.display_requisitions()                                               # Show all stored requests
    # Respond to a request
    request_id_to_respond = int(input("Enter request ID to respond to: "))      # Get request ID to respond
    response_status = input("Enter response status (Approved/Not Approved): ")  # Get the response status
    system.respond_requisition(request_id_to_respond, response_status)          # Respond to the request
    # Display request statistics
    system.requisition_statistic()                                              # Show statistics of requisitions
