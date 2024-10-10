import requests
from jinja2 import Template

class MovieApp:
    def __init__(self, storage):
        """
        Initializes the MovieApp class with a storage object.

        Args:
            storage (IStorage): The storage object to use.
        """
        self._storage = storage


    def _command_list_movies(self):
        """
        Lists all the movies in the storage with their respective year and rating.
        """
        movies = self._storage.list_movies()
        for title, movie in movies.items():
            print(f"{title}: {movie['year']} - Rating: {movie['rating']}")
        

    def _command_movie_stats(self):
        """
        Displays the total number of movies and the average rating of all movies in the storage.

        Prints "No movies found." if the storage is empty.
        """
        movies = self._storage.list_movies()
        total_movies = len(movies)
        if total_movies == 0:
            print("No movies found.")
            return
        total_rating = sum(float(movie['rating']) for movie in movies.values())        
        average_rating = total_rating / total_movies
        print(f"Total movies: {total_movies}")
        print(f"Average rating: {average_rating}")


    def _command_add_movie(self):

        """
        Asks the user for a movie name and adds it to the storage.
        It uses the OMDB API to fetch the movie year and rating.
        If the movie is not found, the user is notified and asked to insert the movie name again.
        """
        while True:
            name = input("Please insert the movie name: ")
            response = requests.get(f"https://www.omdbapi.com/?apikey=6fed4800&t={name}")
            if response.status_code == 200:
                movie = response.json()
                if 'Error' in movie:
                    print("Movie not found.")
                else:
                    poster = movie['Poster']
                    year = movie['Year']
                    rating = movie['imdbRating']
                    self._storage.add_movie(name, year, rating, poster)
                    print(f"Movie {name} : {year} added.")
                    return
            else:
                print("Invalid movie name.")



    def _command_delete_movie(self):
        """
        Asks the user for a movie name and deletes it from the storage.
        If the movie is not found, the user is notified.
        """
        name = input("Please insert the movie name: ")
        self._storage.delete_movie(name)


    def _command_update_movie(self):
        """
        Asks the user for a movie name and its new rate, and updates the movie in the storage.
        If the user enters an invalid movie rate, the user is notified and the user is asked to insert the movie
        information again.
        """
        while True:
            name = input("Please insert the movie name: ")
            while True:
                try:
                    rate = input("Please insert the movie rate (0-10): ")
                    if rate:  # Check if the input is not empty
                        rate = float(rate)
                        if 0 <= rate <= 10:
                            self._storage.update_movie(name, rate)
                            return
                        else:
                            print("Rate out of range! (0-10)")
                    else:
                        print("Please enter a valid rate.")
                except ValueError:
                    print("Invalid input. Please enter a valid rate.")


    def _generate_website(self):
        """
        Generates a website with the movies.
        """
        with open('static/index_template.html', 'r') as file:
            template = Template(file.read())
        
        movies = self._storage.list_movies()
        renderer_template = template.render(movies=movies)

        with open('static/index.html', 'w') as file:
            file.write(renderer_template)

        print("Website was generated successfully.")
        
        


    def run(self):
        """
        Runs the movie app.
        """
        while True:
            print("\nMovie App Menu:")
            print("1. List movies")
            print("2. Movie stats")
            print("3. Add movie")
            print("4. Delete movie")
            print("5. Update movie")
            print("6. Generate website")
            print("7. Quit")
            command = input("Enter command: ")
            if command == "1":
                self._command_list_movies()
            elif command == "2":
                self._command_movie_stats()
            elif command == "3":
                self._command_add_movie()
            elif command == "4":
                self._command_delete_movie()
            elif command == "5":
                self._command_update_movie()
            elif command == "6":
                self._generate_website()
            elif command == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid command. Please try again.")