
"""
The program requests staff members to input the items requested and its price. Total costs is then calculated by 
adding the prices.

Author: Rajiv Akaash Deo
"""
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
