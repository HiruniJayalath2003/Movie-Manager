#define movie class to store information about movie
class Movie:
    def __init__(self, movie_ID, title, director, release_year, genre):
        self.movie_ID = movie_ID
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        
# __str__() use to display objects as a readable srting 
    def __str__(self):
        return (f"ID: {self.movie_ID}, Title: {self.title}, Director: {self.director},Year: {self.release_year}, Genre: {self.genre}")

#define a movie collection class to manage movies
class MovieCollection:
    def __init__(self):
        self.movies = []

    # Add a movie if the movie ID is unique
    def add_movie(self, movie, silent=False):
        if any(item.movie_ID == movie.movie_ID for item in self.movies):
            if not silent:
                print("Error: Movie ID must be unique. Movie not added.")
            return False
        self.movies.append(movie)
        if not silent:
            print("Movie added successfully.")
        return True

    #display all movies
    def view_all_movies(self):
        if not self.movies:
            print("No movies in the collection.")
        else:
            print("\nMovies in collection:")
            for movie in self.movies:
                print(movie)

    #search for a movie
    def search_by_title(self, title):
        found = False
        print(f"\nSearch results for '{title}':")
        for movie in self.movies:
            if title.lower() in movie.title.lower():
                print(movie)
                found = True
        if not found:
            print(f"No movies found with title containing '{title}'.")

    #find a movie by its ID
    def find_movie_by_id(self, movie_ID):
        for movie in self.movies:
            if movie.movie_ID == movie_ID:
                return movie
        return None

    # Update a movie's information
    def update_movie(self, movie_id, title=None, director=None, release_year=None, genre=None):
        movie = self.find_movie_by_id(movie_id)
        if not movie:
            print("Movie not found.")
            return False

        if title:
            movie.title = title
        if director:
            movie.director = director
        if release_year:
            movie.release_year = release_year
        if genre:
            movie.genre = genre

        print("Movie updated successfully.")
        return True

    # Delete a movie by ID
    def delete_movie(self, movie_ID):
        movie = self.find_movie_by_id(movie_ID)
        if movie:
            self.movies.remove(movie)
            print("Movie deleted successfully.")
            return True
        else:
            print("Movie not found.")
            return False  


# Main function that runs the program
def main():
    collection = MovieCollection()

    # enter preloaded movies
    preloaded_movies = [
        {"movie_id": "M001", "title": "La La Land", "director": "Damien Chazelle", "release_year": 2016, "genre": "Romantic"},
        {"movie_id": "M002", "title": "Past Lives", "director": "Celine Song", "release_year": 2023, "genre": "Romantic"},
        {"movie_id": "M003", "title": "A Quiet Place", "director": "John Krasinski", "release_year": 2018, "genre": "Horror"},
        {"movie_id": "M004", "title": "Talk to Me", "director": "Danny & Michael Philippou", "release_year": 2022, "genre": "Horror"},
        {"movie_id": "M005", "title": "Oppenheimer", "director": "Christopher Nolan", "release_year": 2023, "genre": "Historical"},
        {"movie_id": "M006", "title": "The Last Duel", "director": "Ridley Scott", "release_year": 2021, "genre": "Historical"},
        {"movie_id": "M007", "title": "Dune", "director": "Denis Villeneuve", "release_year": 2021, "genre": "Sci-Fi"},
        {"movie_id": "M008", "title": "Everything Everywhere All At Once", "director": "Daniel Kwan & Daniel Scheinert", "release_year": 2022, "genre": "Sci-Fi"},
        {"movie_id": "M009", "title": "Barbie", "director": "Greta Gerwig", "release_year": 2023, "genre": "Comedy"},
        {"movie_id": "M010", "title": "Free Guy", "director": "Shawn Levy", "release_year": 2021, "genre": "Comedy"},
        {"movie_id": "M011", "title": "Top Gun: Maverick", "director": "Joseph Kosinski", "release_year": 2022, "genre": "Action"},
        {"movie_id": "M012", "title": "Extraction", "director": "Sam Hargrave", "release_year": 2020, "genre": "Action"},
        {"movie_id": "M013", "title": "Creed", "director": "Ryan Coogler", "release_year": 2015, "genre": "Sports"},
        {"movie_id": "M014", "title": "King Richard", "director": "Reinaldo Marcus Green", "release_year": 2021, "genre": "Sports"},
        {"movie_id": "M015", "title": "Titanic", "director": "James Cameron", "release_year": 1997, "genre": "Romantic"},
    ]

    # Add each preloaded movie to the collection
    for item in preloaded_movies:
        movie = Movie(item["movie_id"], item["title"], item["director"], item["release_year"], item["genre"])
        collection.add_movie(movie, silent=True)

    # Main menu loop
    while True:
        print("\n--- Movie Collection Manager ---")
        print("1. Add a new movie")
        print("2. View all movies")
        print("3. Search for movies by title")
        print("4. Update a movie")
        print("5. Delete a movie")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            movie_id = input("Enter movie ID: ").strip()
            if collection.find_movie_by_id(movie_id):
                print("This movie ID already exists. Try a different one.")
                continue
            title = input("Enter title: ").strip()
            director = input("Enter director: ").strip()
            release_year = input(int("Enter release year: "))
            genre = input("Enter genre(s): ").strip()

            new_movie = Movie(movie_id, title, director, release_year, genre)
            collection.add_movie(new_movie)

        elif choice == '2':
            collection.view_all_movies()

        elif choice == '3':
            title = input("Enter title to search: ").strip()
            collection.search_by_title(title)

        elif choice == '4':
            movie_id = input("Enter movie ID to update: ").strip()
            movie = collection.find_movie_by_id(movie_id)

            if movie:  
                new_title = input("Enter new title: ").strip()
                new_director = input("Enter new director: ").strip()
                new_release_year = input(int("Enter new release year: "))
                new_genre = input("Enter new genre: ").strip()

                collection.update_movie(movie_id, new_title, new_director, new_release_year, new_genre)
            else:
                print("Movie not found.")

        elif choice == '5':
            movie_id = input("Enter movie ID to delete: ").strip()
            collection.delete_movie(movie_id)

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

#run the program
if __name__ == "__main__":
    main()
