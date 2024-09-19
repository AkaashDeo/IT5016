"""
Create menu System

Author: Akaash Deo
"""  
class Movie:
    def __init__(self, title, genre, year):  # Initialize movie attributes
        self.title = title  # Title of the movie
        self.genre = genre  # Genre of the movie
        self.year = year    # Release year of the movie
        self.available = True  # Status of the movie, initially available
    
    def mark_as_rented(self):  # Mark the movie as rented (not available)
        self.available = False  # Set availability to False

    def mark_as_available(self):  # Mark the movie as available for rent
        self.available = True  # Set availability to True

    def __str__(self):  # Return a string representation of the movie's details
        availability = "Available" if self.available else "Rented"  # Check availability status
        return f"{self.title} - {self.year} - Genre: {self.genre}, Status: {availability}"


# Customer Class: Manages customer details and their rented movies.
class Customer:
    def __init__(self, name):  # Initialize customer attributes
        self.name = name  # Name of the customer
        self.rented_movies = []  # List to keep track of rented movies

    def rent_movie(self, movie):  # Rent a movie if it is available
        if movie.available:  # Check if the movie is available
            movie.mark_as_rented()  # Mark the movie as rented
            self.rented_movies.append(movie)  # Add the movie to the rented list
            print(f"Rented: {movie.title}")  # Notify that the movie is rented
        else:
            print(f"{movie.title} is not available.")  # Notify if the movie is not available

    def return_movie(self, movie):  # Return a rented movie
        if movie in self.rented_movies:  # Check if the movie is rented by the customer
            movie.mark_as_available()  # Mark the movie as available
            self.rented_movies.remove(movie)  # Remove the movie from the rented list
            print(f"Returned: {movie.title}")  # Notify that the movie is returned
        else:
            print(f"Error: {movie.title} is not rented by you.")  # Notify if the movie was not rented by the customer

    def list_rented_movies(self):  # List all movies currently rented by the customer
        if self.rented_movies:  # Check if there are rented movies
            print(f"{self.name}'s Rented Movies:")  # Header for rented movies list
            for movie in self.rented_movies:  # Loop through each rented movie
                print(f"- {movie}")  # Print each rented movie
        else:
            print(f"{self.name} has no rented movies.")  # Notify if no movies are rented


# Rental Store Class: Manages the movie inventory and customer interactions.
class RentalStore:
    def __init__(self):  # Initialize store attributes
        self.movies = []  # List to store available movies in the store

    def add_movie(self, movie):  # Add a movie to the store's inventory
        self.movies.append(movie)  # Add movie to the list
        print(f"Movie added: {movie.title}")  # Notify that the movie was added

    def list_movies(self):  # List all available movies in the store
        if self.movies:  # Check if there are any movies in the store
            print("Available Movies in Store:")  # Header for available movies list
            for movie in self.movies:  # Loop through each movie
                if movie.available:  # Check if the movie is available
                    print(f"- {movie}")  # Print each available movie
        else:
            print("No movies available in the store.")  # Notify if no movies are available

    def find_movie(self, title):  # Find a movie by its title
        for movie in self.movies:  # Loop through each movie in the store
            if movie.title.lower() == title.lower():  # Compare titles case-insensitively
                return movie  # Return the movie if found
        print("Movie not found.")  # Notify if the movie was not found
        return None  # Return None if the movie is not in the store


""" 
Task 2

Author: Rajiv Deo

"""
# Function to display the menu options for the movie rental system
def display_menu():  # Display menu options
    print("\nMovie Rental System")  # Header for the rental system
    print("1. List available movies")  # Option to list all available movies
    print("2. Rent a movie")           # Option to rent a movie
    print("3. Return a movie")         # Option to return a rented movie
    print("4. List rented movies for a specific customer")  # Option to list movies rented by a specific customer
    print("5. Add a new movie to the store")  # Option to add a new movie to the store
    print("6. Exit")  # Option to exit the system

# Main menu function to handle user interactions
def main_menu():  # Main function for user interaction
    store = RentalStore()  # Create an instance of RentalStore
    customers = {}  # Dictionary to keep track of customers

    while True:  # Infinite loop for menu options
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Get user choice

        if choice == '1':  # User chose to list available movies
            store.list_movies()  # List all available movies in the store

        elif choice == '2':  # User chose to rent a movie
            customer_name = input("Enter your name: ")  # Get the customer's name
            if customer_name not in customers:  # Check if customer exists
                customers[customer_name] = Customer(customer_name)  # Create a new customer if not already in the dictionary
            customer = customers[customer_name]  # Retrieve the customer object
            title = input("Enter movie title to rent: ")  # Get the title of the movie to rent
            movie = store.find_movie(title)  # Find the movie in the store
            if movie:  # Check if movie is found
                customer.rent_movie(movie)  # Rent the movie if found

        elif choice == '3':  # User chose to return a movie
            customer_name = input("Enter your name: ")  # Get the customer's name
            if customer_name not in customers:  # Check if customer exists
                print("Customer not found.")  # Notify if the customer does not exist
                continue  # Continue to the next iteration
            customer = customers[customer_name]  # Retrieve the customer object
            title = input("Enter movie title to return: ")  # Get the title of the movie to return
            movie = store.find_movie(title)  # Find the movie in the store
            if movie:  # Check if movie is found
                customer.return_movie(movie)  # Return the movie if found

        elif choice == '4':  # User chose to list rented movies
            customer_name = input("Enter your name: ")  # Get the customer's name
            if customer_name not in customers:  # Check if customer exists
                print("Customer not found.")  # Notify if the customer does not exist
                continue  # Continue to the next iteration
            customer = customers[customer_name]  # Retrieve the customer object
            customer.list_rented_movies()  # List all movies currently rented by the customer

        elif choice == '5':  # User chose to add a new movie
            title = input("Enter movie title: ")  # Get the movie title
            genre = input("Enter movie genre: ")  # Get the movie genre
            year = input("Enter release year: ")  # Get the movie release year
            movie = Movie(title, genre, year)  # Create a new movie instance
            store.add_movie(movie)  # Add the movie to the store

        elif choice == '6':  # User chose to exit
            print("Exiting the system.")  # Notify that the system is exiting
            break  # Exit the while loop to terminate the program

        else:  # Invalid choice
            print("Invalid choice. Please try again.")  # Notify if the choice is invalid

# Entry point of the program
if __name__ == "__main__":  # Check if the script is being run directly
    main_menu()  # Call the main_menu function to start the program
