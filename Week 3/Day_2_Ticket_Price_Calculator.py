"""
The following shows how to code trace.

Author: Akaash Deo
"""

def get_price(adult, child):                                  # Function to calculate the price based on number of adults and children.
    child_price = 10                                          # Set the price for a child ticket.
    adult_price = 25                                          # Set the price for an adult ticket.
    group_size = 14                                           # Define the group size for discounts.
    group_rate = 0.9                                          # Set the group discount rate.

    cost = (child * child_price + adult * adult_price)        # Calculate total cost based on number of tickets.

    if child + adult > group_size:                            # Check if the total number of tickets exceeds the group size.
        cost = cost * group_rate                              # Apply discount if above group size.
    
    return cost                                               # Return the calculated cost.

def main():                                                   # Main function for user inputs and outputs.
    num_child = int(input("Enter the number of children: "))  # Prompt for number of children.
    num_adult = int(input("Enter the number of adults: "))    # Prompt for number of adults.
    cost = get_price(num_adult, num_child)                    # Call get_price function with user inputs.
    print("The cost of your tickets is: $" + str(cost))       # Print the total cost, converting to string for concatenation.

main()                                                        # Call the main function to execute the program.
