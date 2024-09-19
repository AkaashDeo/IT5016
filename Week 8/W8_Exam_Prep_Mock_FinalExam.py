
#Mock Exam

#Task 1: `staff_info` Function

#Question:*

"""
1.1: Write a Python function named `staff_info` that generates a unique ID internally. 
The function should prompt the user for the following details:
- Date
- Staff ID
- Staff Name

Ensure that the `uniqueID` is generated within the function by adding 10000 to a counter passed to the function. 
Print the collected information and the generated unique ID.

1.2: Explain how the function ensures that each generated ID is unique.

2.1: Write a Python function named `requisition_total` that collects item names and their prices from the user until 
they decide not to add more items. The function should calculate and return the total sum of the item prices.

2.2: Explain how the function calculates the total sum and handles the loop exit condition.

3.1: Write a Python function named `requisition_approval` that takes the staff ID, unique ID, and total sum of a requisition. 
It should return "Approved" if the total is less than $500 and "Pending" otherwise. 

Also, generate a reference number if approved, using the last three digits of the unique ID concatenated with the staff ID.

3.2: Explain how the function determines the approval status and generates the reference number.

Write a Python function named `display_requisitions` that integrates the functionality of `staff_info`, 
`requisition_total`, and `requisition_approval`. It should collect staff details, request items, determine approval,
 and print all relevant information in a formatted manner.

4.2: Explain how the function integrates different tasks and handles displaying results.

5.1: Create a Python class named `MembershipSystem` to manage student memberships. The class should have methods for registering students, withdrawing memberships, and displaying member statistics. It should track the number of registered members, students in each programme, and withdrawn members.

5.2: Explain how the class methods handle registration, withdrawal, and displaying statistics.


"""


# Solution:

def staff_info(counter):
    """Generates a unique ID and collects staff information."""
    # Prompt the user for details
    date = input("Enter Date: ")
    staffID = input("Enter Staff ID: ")
    name = input("Enter Staff Name: ")

    # Generate unique ID by adding 10000 to the counter
    uniqueID = counter + 10000
    
    # Print the collected information and the unique ID
    print(f"\nPrinting Staff Information:")
    print(f"Date: {date}")
    print(f"Staff ID: {staffID}")
    print(f"Staff Name: {name}")
    print(f"Requisition ID: {uniqueID}")

    return staffID, uniqueID, date, name

# Initialize counter and call function
counter = 1000
staff_info(counter)


# Explanation:
"""The function `staff_info` uses a `counter` to generate a unique ID by adding a fixed number (10000) to it. 
This ensures that each ID is unique as long as the counter increments with each call."""

#Task 2: `requisition_total` Function

#Question:

"""2.1: Write a Python function named `requisition_total` that collects item names and their prices from the user until 
they decide not to add more items. The function should calculate and return the total sum of the item prices.

2.2: Explain how the function calculates the total sum and handles the loop exit condition."""

#Solution:

def requisition_total():
    """Collects item names and prices, calculates the total sum."""
    total_sum = 0

    while True:
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))

        # Calculate total sum directly
        total_sum += price

        another = input("Add another item? (y/n): ")
        if another.lower() != "y":
            break

    print(f"Total: ${total_sum:.2f}")
    return total_sum

# Call the function
requisition_total()


# Explanation
"""The function collects items and their prices in a list until the user indicates they are done. 
The total sum is calculated by iterating through the list of items and summing their prices. 
The loop exits when the user inputs something other than 'y'.
"""

# Task 3: `requisition_approval` Function

#Question:

"""3.1: Write a Python function named `requisition_approval` that takes the staff ID, unique ID, and total sum of a requisition. 
It should return "Approved" if the total is less than $500 and "Pending" otherwise. 

Also, generate a reference number if approved, using the last three digits of the unique ID concatenated with the staff ID.

3.2: Explain how the function determines the approval status and generates the reference number."""

#Solution:

def requisition_approval(staffID, uniqueID, total_sum):
    """Determines the approval status and generates a reference number if approved."""
    if total_sum < 500:
        status = "Approved"
        id_str = str(uniqueID)
        ref_num = str(staffID) + id_str[-3:]
        print(f"\nTotal: ${total_sum:.2f}\nStatus: {status}\nApproval Reference Number: {ref_num}")
    else:
        status = "Pending"
        ref_num = None
        print(f"\nTotal: ${total_sum:.2f}\nStatus: {status}")

    return status, ref_num

# Example call to the function
requisition_approval(123, 456789, 450)


# Explanation
""" 
The function evaluates if the total sum is below $500 to determine the status. If approved, it generates a reference number using the last three digits of the unique ID concatenated with the staff ID.
"""


#Task 4: `display_requisitions` Function

#Question:

""" 
4.1: Write a Python function named `display_requisitions` that integrates the functionality of `staff_info`, 
`requisition_total`, and `requisition_approval`. It should collect staff details, request items, determine approval,
 and print all relevant information in a formatted manner.

4.2: Explain how the function integrates different tasks and handles displaying results."""

#Solution:

def display_requisitions():
    """Displays a complete requisition including staff info, total, and approval status."""
    global counter
    staffID, uniqueID, date, name = staff_info(counter)
    total_sum = requisition_total()
    status, ref_num = requisition_approval(staffID, uniqueID, total_sum)

    print(f"\nPrinting Requisition:\nDate: {date}\nRequisition ID: {uniqueID}\nStaff ID: {staffID}\nStaff Name: {name}\nTotal: ${total_sum:.2f}\nStatus: {status}\nApproval Reference Number: {ref_num if ref_num else 'N/A'}\n")

# Initialize counter and call the function
counter = 1000
display_requisitions()



"""Explanation: 
The function `display_requisitions` calls the other functions to gather staff information, calculate totals, 
and determine approval. It then prints all relevant details in a clear and formatted manner.
"""


# Task 5: Membership Registration System

#Question:

"""5.1: Create a Python class named `MembershipSystem` to manage student memberships. The class should have methods for registering students, withdrawing memberships, and displaying member statistics. It should track the number of registered members, students in each programme, and withdrawn members.

5.2: Explain how the class methods handle registration, withdrawal, and displaying statistics."""

#Solution

class MembershipSystem:
    membership_id_counter = 1000
    registered_members = []
    withdrawn_count = 0

    def __init__(self):
        self.diploma_count = 0
        self.bachelor_count = 0

    def register_student(self):
        """Registers a new student member."""
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Student Last Name: ")
        programme = input("Enter Student Programme (Diploma/Bachelor): ").capitalize()

        if programme not in ["Diploma", "Bachelor"]:
            print("Invalid programme. Must be 'Diploma' or 'Bachelor'.")
            return

        membership_id = MembershipSystem.membership_id_counter
        MembershipSystem.membership_id_counter += 1

        member = {
            'membership_id': membership_id,
            'student_id': student_id,
            'last_name': last_name,
            'programme': programme
        }

        MembershipSystem.registered_members.append(member)

        if programme == "Diploma":
            self.diploma_count += 1
        else:
            self.bachelor_count += 1

        print(f"Student registered successfully with Membership ID: {membership_id}")

    def withdraw_student(self):
        """Withdraws a student from the membership."""
        membership_id = int(input("Enter Membership ID to withdraw: "))
        last_name = input("Enter Student Last Name: ")

        for member in MembershipSystem.registered_members:
            if member['membership_id'] == membership_id and member['last_name'] == last_name:
                MembershipSystem.registered_members.remove(member)

                if member['programme'] == "Diploma":
                    self.diploma_count -= 1
                else:
                    self.bachelor_count -= 1

                MembershipSystem.withdrawn_count += 1

                print(f"Student with Membership ID {membership_id} has been withdrawn.")
                return

        print("No matching member found for withdrawal.")

    def display_members(self):
        """Displays information about registered members."""
        num_registered_members = len(MembershipSystem.registered_members)

        print(f"\nNumber of Registered Members: {num_registered_members}")
        print(f"Number of Diploma Students: {self.diploma_count}")
        print(f"Number of Bachelor Students: {self.bachelor_count}")
        print(f"Number of Withdrawn Students: {MembershipSystem.withdrawn_count}")

        print("\nRegistered Members:")
        for member in MembershipSystem.registered_members:
            print(f"Membership ID: {member['membership_id']}, Student ID: {member['student_id']}, Last Name: {member['last_name']}, Programme: {member['programme']}")

# Example usage
if __name__ == "__main__":
    system = MembershipSystem()

    system.register_student()
    system.register_student()
    system.withdraw_student()
    system.display_members()

# Explanation
"""
The `MembershipSystem` class handles registration by adding new members to a list and updating counts based on their programme. Withdrawal involves removing a member from the list and updating counts. The `display_members` method provides an overview of all members, including statistics and individual details.
"""

#Task 6: Software Development Life Cycle (SDLC)

#Question

"""6.1: Identify and explain the different stages of

 the Software Development Life Cycle (SDLC) and their importance."""

#Solution:

"""
1. Planning

Overview:
In the planning phase, you outline the goals and requirements for the code tasks. 
For the provided tasks, planning involves determining the overall functionality needed: a system to 
manage staff requisitions, item totals, approvals, and a membership registration system.

Key Activities:
- Define Objectives: Identify the need for a function to handle staff information, item requisitions, requisition approvals, and a membership management system.
- Resource Planning: Allocate resources for coding, testing, and documentation. Identify team members or tools needed for development.
- Timeline: Set deadlines for each task, ensuring that functions and the class are developed and tested systematically.

2. Requirement Analysis

Overview:
The requirement analysis phase involves gathering and documenting detailed requirements for each function and class. 
This ensures that the final code will meet user needs and project goals.

Key Activities:
- **Gather Requirements:** Determine that `staff_info` should generate a unique ID, `requisition_total` should calculate totals from user input, `requisition_approval` should handle approval logic, and `MembershipSystem` should manage student memberships.
- **Document Requirements:** Create specifications for each function and class. For example, `staff_info` must generate a unique ID and display staff details, while `MembershipSystem` must track and manage student memberships.

3. Design

Overview:
Design involves creating a blueprint for how the code will be structured.
 This includes defining the functions and class, their interactions, and how they will achieve the desired functionality.

Key Activities:
- System Architecture: Design the `staff_info`, `requisition_total`, and `requisition_approval` functions, and the 
`MembershipSystem` class.
- Detailed Design: Specify the internal logic of each function and class. 
For instance, design how `staff_info` generates unique IDs, how `requisition_total` calculates totals, and 
how `MembershipSystem` manages registrations and withdrawals.
- Prototyping: Optionally create prototypes or pseudo-code to outline the logic of each function and class.


4. Implementation

Overview:
The implementation phase involves writing the actual code based on the design. 
This is where the functions and class are developed and coded.

Key Activities:
- Coding:Write the code for `staff_info`, `requisition_total`, `requisition_approval`, `display_requisitions`, and the 
`MembershipSystem` class.
- Unit Testing: Test individual functions and methods to ensure they work as intended.

5. Testing

Overview:
The testing phase involves verifying that the code works correctly and meets the requirements. 
This includes functional testing, integration testing, and fixing any issues found.

Key Activities:
- Test Planning:Develop a test plan for each function and class, including test cases for different scenarios.
- Test Execution:Execute the test cases for `staff_info`, `requisition_total`, `requisition_approval`, `display_requisitions`, and `MembershipSystem` to ensure they work correctly.
- Defect Management:Identify and fix any bugs or issues found during testing.


6. Maintenance

Overview:
Maintenance involves making updates and providing support after the code is deployed. 
This includes fixing bugs, adding new features, and ensuring the system continues to function correctly.

Key Activities:
- Bug Fixes: Address any issues or defects reported by users after deployment.
- Enhancements: Implement new features or improvements based on user feedback or changing requirements.
- Support: Provide ongoing support and updates to ensure the system remains functional and up-to-date.


By following these stages—Planning, Requirement Analysis, Design, Implementation, Testing, and Maintenance —

you ensure that the code tasks are developed systematically, meet the specified requirements, and are maintained effectively 
throughout their lifecycle.
"""