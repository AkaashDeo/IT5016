"""
TASK 1

Develop a Python-based movie rental system using Object-Oriented Programming
(OOP). This system will include classes for managing movies, customers, and a rental
store. You will also create a text-based menu to interact with the system.

Requirements:

1. Define the Classes:
Movie Class, Customer Class, Rental Store Class

Attributes:

▪ title: The title of the movie.
▪ genre: The genre of the movie.
▪ year: The release year of the movie.
▪ available: A boolean indicating whether the movie is
available for rent.

Methods:

▪ mark_as_rented(): Marks the movie as rented.
▪ mark_as_available(): Marks the movie as available.
▪ __str__(): Provides a string representation of the movie's
details.

Author: Rajiv Deo
"""
# Movie Class: Manages movie details and status.
class Movie:
    def __init__(self, title, genre, year):
        # Initialize movie attributes
        self.title = title  # Title of the movie
        self.genre = genre  # Genre of the movie
        self.year = year    # Release year of the movie
        self.available = True  # Status of the movie, initially available
    
    def mark_as_rented(self):
        # Mark the movie as rented (not available)
        self.available = False

    def mark_as_available(self):
        # Mark the movie as available for rent
        self.available = True

    def __str__(self):
        # Return a string representation of the movie's details
        availability = "Available" if self.available else "Rented"
        return f"{self.title} - {self.year} - Genre: {self.genre}, Status: {availability}"


# Customer Class: Manages customer details and their rented movies.
class Customer:
    def __init__(self, name):
        # Initialize customer attributes
        self.name = name  # Name of the customer
        self.rented_movies = []  # List to keep track of rented movies

    def rent_movie(self, movie):
        # Rent a movie if it is available
        if movie.available:
            movie.mark_as_rented()  # Mark the movie as rented
            self.rented_movies.append(movie)  # Add the movie to the rented list
            print(f"Rented: {movie.title}")  # Notify that the movie is rented
        else:
            print(f"{movie.title} is not available.")  # Notify if the movie is not available

    def return_movie(self, movie):
        # Return a rented movie
        if movie in self.rented_movies:
            movie.mark_as_available()  # Mark the movie as available
            self.rented_movies.remove(movie)  # Remove the movie from the rented list
            print(f"Returned: {movie.title}")  # Notify that the movie is returned
        else:
            print(f"Error: {movie.title} is not rented by you.")  # Notify if the movie was not rented by the customer

    def list_rented_movies(self):
        # List all movies currently rented by the customer
        if self.rented_movies:
            print(f"{self.name}'s Rented Movies:")  # Header for rented movies list
            for movie in self.rented_movies:
                print(f"- {movie}")  # Print each rented movie
        else:
            print(f"{self.name} has no rented movies.")  # Notify if no movies are rented


# Rental Store Class: Manages the movie inventory and customer interactions.
class RentalStore:
    def __init__(self):
        # Initialize store attributes
        self.movies = []  # List to store available movies in the store

    def add_movie(self, movie):
        # Add a movie to the store's inventory
        self.movies.append(movie)  # Add movie to the list
        print(f"Movie added: {movie.title}")  # Notify that the movie was added

    def list_movies(self):
        # List all available movies in the store
        if self.movies:
            print("Available Movies in Store:")  # Header for available movies list
            for movie in self.movies:
                if movie.available:
                    print(f"- {movie}")  # Print each available movie
        else:
            print("No movies available in the store.")  # Notify if no movies are available

    def find_movie(self, title):
        # Find a movie by its title
        for movie in self.movies:
            if movie.title.lower() == title.lower():  # Compare titles case-insensitively
                return movie  # Return the movie if found
        print("Movie not found.")  # Notify if the movie was not found
        return None  # Return None if the movie is not in the store






















# Example usage of the movie rental system
def main():
    store = RentalStore()  # Create a rental store instance

    # Adding movies to the rental store
    movie1 = Movie("Inception", "Sci-Fi", 2010)  # Create a new movie instance
    movie2 = Movie("The Matrix", "Action", 1999)  # Create another movie instance
    store.add_movie(movie1)  # Add the first movie to the store
    store.add_movie(movie2)  # Add the second movie to the store

    customer = Customer("Alice")  # Create a new customer instance

    # Listing available movies
    store.list_movies()  # Print all available movies in the store

    # Renting a movie
    movie_to_rent = store.find_movie("Inception")  # Find the movie to rent
    if movie_to_rent:
        customer.rent_movie(movie_to_rent)  # Rent the movie if it was found

    # Listing rented movies
    customer.list_rented_movies()  # Print all movies currently rented by the customer

    # Returning a movie
    customer.return_movie(movie_to_rent)  # Return the movie

    # Listing rented movies after return
    customer.list_rented_movies()  # Print the list of rented movies after returning one

    # Listing available movies after return
    store.list_movies()  # Print all available movies in the store after returning a movie

if __name__ == "__main__":
    main()  # Run the main function to execute the example usage
