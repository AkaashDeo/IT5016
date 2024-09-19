"""
Improvements  Made: 

Enhance the menu to handle multiple customers and their interactions better. 
The current setup creates a new `Customer` instance each time, which is not practical for a real-world application. 
For a more realistic system, you would want to maintain a list or database of customers and manage their state 
across different menu options.


- Customer Management: 
Introduced a dictionary customers to keep track of existing customers by their name. 
This ensures that the same customer can be referenced across different interactions.

- Customer Lookup: 
Before performing any operation (renting, returning, listing rented movies), 
the program checks if the customer already exists in the dictionary. 
If not, it creates a new Customer instance and adds it to the dictionary.

With these updates, the system now correctly handles multiple customers and their interactions with the movie rental system.

How:

- Modify the main_menu function to handle multiple customers more effectively. 
- Instead of creating a new Customer instance each time, 
I'll maintain a dictionary of customers to keep track of them and allow multiple interactions with the same customer.

Author: Rajiv Deo

"""
# Define the Movie class to handle movie-related operations
class Movie:
    def __init__(self, title, genre, year):
        self.title = title           # Movie title
        self.genre = genre           # Movie genre
        self.year = year             # Release year of the movie
        self.available = True       # Movie availability status, default is True (available)

    def mark_as_rented(self):
        self.available = False      # Set movie availability to False (rented)

    def mark_as_available(self):
        self.available = True       # Set movie availability to True (available)

    def __str__(self):
        availability = "Available" if self.available else "Rented"
        # Return a string representation of the movie's details
        return f"Title: {self.title}, Genre: {self.genre}, Year: {self.year}, Status: {availability}"


# Define the Customer class to manage customer-related operations
class Customer:
    def __init__(self, name):
        self.name = name             # Customer's name
        self.rented_movies = []      # List to keep track of rented movies

    def rent_movie(self, movie):
        if movie.available:
            movie.mark_as_rented()   # Mark movie as rented
            self.rented_movies.append(movie)  # Add movie to customer's rented list
            print(f"Successfully rented: {movie.title}")
        else:
            print(f"Sorry, {movie.title} is not available.")

    def return_movie(self, movie):
        if movie in self.rented_movies:
            movie.mark_as_available()  # Mark movie as available
            self.rented_movies.remove(movie)  # Remove movie from customer's rented list
            print(f"Successfully returned: {movie.title}")
        else:
            print(f"Error: {movie.title} is not rented by you.")

    def list_rented_movies(self):
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")
            for movie in self.rented_movies:
                print(f"- {movie}")  # Print each rented movie's details
        else:
            print(f"{self.name} has no rented movies.")


# Define the RentalStore class to manage the movie rental store operations
class RentalStore:
    def __init__(self):
        self.movies = []           # List to keep track of all movies in the store

    def add_movie(self, movie):
        self.movies.append(movie)  # Add a movie to the store
        print(f"Movie added: {movie.title}")

    def list_movies(self):
        if self.movies:
            print("Available Movies in Store:")
            for movie in self.movies:
                if movie.available:
                    print(f"- {movie}")  # Print details of available movies
        else:
            print("No movies available in the store.")

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie        # Return the movie if found
        print("Movie not found.")  # Inform user if the movie is not found
        return None


# Define the main_menu function to interact with the user and handle menu options
def main_menu():
    store = RentalStore()         # Create an instance of RentalStore
    customers = {}               # Dictionary to keep track of customers

    while True:
        print("\nMovie Rental System")
        print("1. Add Movie")
        print("2. List Movies")
        print("3. Rent Movie")
        print("4. Return Movie")
        print("5. List Rented Movies")
        print("6. Exit")

        choice = input("Enter your choice: ")  # Get user's menu choice

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            year = input("Enter release year: ")
            movie = Movie(title, genre, year)  # Create a new Movie instance
            store.add_movie(movie)             # Add the movie to the store

        elif choice == '2':
            store.list_movies()                # List all available movies in the store

        elif choice == '3':
            customer_name = input("Enter your name: ")
            if customer_name not in customers:
                customers[customer_name] = Customer(customer_name)  # Create a new Customer if not exists
            customer = customers[customer_name]   # Retrieve the Customer instance
            title = input("Enter movie title to rent: ")
            movie = store.find_movie(title)       # Find the movie by title
            if movie:
                customer.rent_movie(movie)       # Rent the movie if available

        elif choice == '4':
            customer_name = input("Enter your name: ")
            if customer_name not in customers:
                customers[customer_name] = Customer(customer_name)  # Create a new Customer if not exists
            customer = customers[customer_name]   # Retrieve the Customer instance
            title = input("Enter movie title to return: ")
            movie = store.find_movie(title)       # Find the movie by title
            if movie:
                customer.return_movie(movie)     # Return the movie if rented by the customer

        elif choice == '5':
            customer_name = input("Enter your name: ")
            if customer_name not in customers:
                customers[customer_name] = Customer(customer_name)  # Create a new Customer if not exists
            customer = customers[customer_name]   # Retrieve the Customer instance
            customer.list_rented_movies()         # List all rented movies by the customer

        elif choice == '6':
            print("Exiting the system.")        # Exit message
            break                             # Break out of the loop to exit the program

        else:
            print("Invalid choice. Please try again.")  # Inform the user of an invalid choice


# Entry point of the program
if __name__ == "__main__":
    main_menu()                      # Call the main_menu function to start the program
