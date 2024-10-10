from movie_app import MovieApp
from storage_csv import StorageCsv

storage = StorageCsv('data/movies.csv')
movie_app = MovieApp(storage)
movie_app.run()