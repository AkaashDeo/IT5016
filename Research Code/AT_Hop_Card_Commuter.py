
"""
Hop Card Personal Checker Program

This program simulates the management of a Hop Card for public transport in Auckland. It allows users 
to track their balance, deposit funds, and manage commutes to and from the university, all while 
interacting in a user-friendly manner.

Author: Akaash Deo
"""


class HopCard:
    """
    Represents a Hop Card for public transport usage.
    
    Attributes:
        card_number (str): The unique number of the hop card.
        __balance (float): The private balance of the hop card.
        owner (str): The name of the card owner.
    """
    
    default_balance = 0.0                                      # Class variable for default balance

    def __init__(self, card_number):                            # Constructor to initialize the HopCard
        self.card_number = card_number                          # Use the provided card number
        self.__balance = HopCard.default_balance                # Initialize the private balance with the default value
        self.owner = ""                                         # Initialize owner name

    def deposit(self, amount):                                  # Method to deposit money
        """Adds money to the hop card if the amount is positive."""
        if amount > 0:                                          # Check if the amount is positive
            self.__balance += amount                            # Update the balance
            print(f"${amount:.2f} has been added to {self.owner}'s hop card.")  # Confirmation message
        else:
            print("Deposit amount must be positive.")           # Error message for invalid deposit

    def withdraw(self, amount):                                 # Method to withdraw money
        """Deducts money from the hop card if there is sufficient balance."""
        if 0 < amount <= self.__balance:                       # Check if the amount is positive and less than or equal to balance
            self.__balance -= amount                            # Update the balance
            print(f"${amount:.2f} has been deducted from {self.owner}'s hop card.")  # Confirmation message
        elif amount <= 0:
            print("Withdrawal amount must be positive.")        # Error message for invalid withdrawal
        else:
            print("Insufficient balance for this transaction.")  # Error message for insufficient funds

    def get_balance(self):                                      # Method to get the current balance
        """Returns the current balance of the hop card."""
        return self.__balance                                   # Return the private balance


class UniversityCommute(HopCard):
    """
    Represents a university commute using a Hop Card.
    
    Inherits from the HopCard class and adds features for commuting.
    
    Attributes:
        fare (float): The fare for commuting to the university.
    """
    
    def __init__(self, card_number):                            # Constructor to initialize UniversityCommute
        super().__init__(card_number)                          # Initialize the parent HopCard class
        self.fare = 4.80                                       # Set the discounted student fare

    def commute_to_university(self):                           # Method for commuting to university
        """Simulates commuting to the university using the hop card."""
        print(f"{self.owner} is commuting from West Auckland to the university.")  # Commute message
        self.withdraw(self.fare)                               # Withdraw the fare from the hop card

    def commute_back_home(self):                               # Method for commuting back home
        """Simulates commuting back home using the hop card."""
        print(f"{self.owner} is commuting back from the university to West Auckland.")  # Commute message
        self.withdraw(self.fare)                               # Withdraw the fare from the hop card


# Personal Checker Interface
def personal_checker():
    """Main interface for the personal hop card checker."""
    print("\nWelcome to your Hop Card Personal Checker!")        # Welcome message

    name = input("\nPlease enter your name: ")                  # Prompt for the user's name
    card_number = input("\nPlease enter your Hop Card number: ") # Prompt for the user's card number

    # Create an instance of UniversityCommute
    card = UniversityCommute(card_number)                      # Create an instance of UniversityCommute
    card.owner = name                                          # Assign the user's name to the card owner

    print(f"\nYour Hop Card Number: {card.card_number}")      # Show the card number

    while True:                                                # Main loop for user options
        print("\nChoose an option:")
        print("\n1. Check Balance")
        print("2. Deposit Funds")
        print("3. Commute to University")
        print("4. Commute Back Home")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")          # Get user choice

        if choice == '1':                                    # Check balance
            balance = card.get_balance()                      # Get current balance
            print(f"{name}, your current balance: ${balance:.2f}")  # Display balance
        elif choice == '2':                                  # Deposit funds
            amount = float(input("Enter amount to deposit: "))  # Get deposit amount
            card.deposit(amount)                               # Deposit the amount
        elif choice == '3':                                  # Commute to university
            if card.get_balance() >= card.fare:              # Check balance for fare
                card.commute_to_university()                 # Commute to university
            else:
                print(f"{name}, insufficient balance to commute to university.")  # Message for insufficient balance
        elif choice == '4':                                  # Commute back home
            if card.get_balance() >= card.fare:              # Check balance for fare
                card.commute_back_home()                      # Commute back home
            else:
                print(f"{name}, insufficient balance to commute back home.")  # Message for insufficient balance
        elif choice == '5':                                  # Exit
            print(f"Thank you for using the Hop Card Personal Checker, {name}. Goodbye!")  # Exit message
            break                                             # Exit the loop
        else:
            print("Invalid choice. Please try again.")       # Error message for invalid choice


# Run the personal checker interface
if __name__ == "__main__":
    personal_checker()                                         # Start the personal checker
