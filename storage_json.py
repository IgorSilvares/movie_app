from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Initializes the StorageJson class with a file path.

        Args:
            file_path (str): The path to the JSON file.
        """
        self.file_path = file_path
        self.movies = self.load_movies()

    def load_movies(self):
        """
        Loads the movies from the JSON file.

        Returns:
            dict: A dictionary containing the movies.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_movies(self):
        """
        Saves the movies to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.movies, file, indent=4)

    def list_movies(self):
        """
        Lists all the movies in the storage.

        Returns:
            dict: A dictionary containing the movies.
        """
        return self.movies

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the storage.

        Args:
            title (str): The title of the movie.
            year (int): The year of the movie.
            rating (float): The rating of the movie.
            poster (str): The poster of the movie.
        """
        if title in self.movies:
            print("Movie already exists.")
            return
        self.movies[title] = {
            'year': year,
            'rating': rating,
            'poster': poster
        }
        self.save_movies()

    def delete_movie(self, title):
        """
        Deletes a movie from the storage.

        Args:
            title (str): The title of the movie.
        """
        if title not in self.movies:
            print("Movie not found.")
            return
        del self.movies[title]
        self.save_movies()

    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the storage.

        Args:
            title (str): The title of the movie.
            rating (float): The new rating of the movie.
        """
        if title not in self.movies:
            print("Movie not found.")
            return
        self.movies[title]['rating'] = rating
        self.save_movies()



