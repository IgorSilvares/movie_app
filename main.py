from movie_app import MovieApp
from storage_json import StorageJson

def main():
    """
    The main entry point of the program. Initializes the MovieApp class with a StorageJson object and calls its run method.
    """
    storage = StorageJson("data/igor_movies.json")
    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    main()