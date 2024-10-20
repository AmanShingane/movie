import json
import os

# Define the file where movies will be stored
MOVIE_FILE = "movies.json"

def load_movies():
    if os.path.exists(MOVIE_FILE):
        with open(MOVIE_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_movies(movies):
    with open(MOVIE_FILE, "w") as file:
        json.dump(movies, file, indent=4)

def add_movie():
    name = input("Enter movie name: ")
    director = input("Enter movie director: ")
    year = int(input("Enter movie year: "))
    location = input("Enter movie location: ")
    shelf = input("Enter movie shelf: ")
    movie = {
        'name': name,
        'director': director,
        'year': year,
        'location': location,
        'shelf': shelf
    }
    movies = load_movies()
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully!")

def view_all_movies():
    movies = load_movies()
    if not movies:
        print("No movies in the collection.")
    else:
        print("Movie Collection:")
        for index, movie in enumerate(movies, start=1):
            print(f"Movie {index}:")
            print(f"Name: {movie['name']}")
            print(f"Director: {movie['director']}")
            print(f"Year: {movie['year']}")
            print(f"Location: {movie['location']}")
            print(f"Shelf: {movie['shelf']}")
            print("------------------------")

def find_movie():
    movies = load_movies()
    if not movies:
        print("No movies in the collection.")
    else:
        property = input("Enter property to search (e.g., year, director): ")
        value = input("Enter value to search for: ")
        results = [movie for movie in movies if str(movie.get(property)) == value]
        if results:
            print("Found the following movies:")
            for index, movie in enumerate(results, start=1):
                print(f"Movie {index}:")
                print(f"Name: {movie['name']}")
                print(f"Director: {movie['director']}")
                print(f"Year: {movie['year']}")
                print(f"Location: {movie['location']}")
                print(f"Shelf: {movie['shelf']}")
                print("------------------------")
        else:
            print("No movies found.")

def delete_movie():
    movies = load_movies()
    if not movies:
        print("No movies in the collection.")
    else:
        view_all_movies()
        movie_number = int(input("Enter the number of the movie to delete: "))
        try:
            del movies[movie_number - 1]
            save_movies(movies)
            print("Movie deleted successfully!")
        except IndexError:
            print("Invalid movie number.")

while True:
    print("Movie Storage Application")
    print("1. Add a new movie")
    print("2. View all movies")
    print("3. Find a movie")
    print("4. Delete a movie")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_movie()
    elif choice == "2":
        view_all_movies()
    elif choice == "3":
        find_movie()
    elif choice == "4":
        delete_movie()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")