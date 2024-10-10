from istorage import IStorage
import csv

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self.load_movies()

    def load_movies(self):
        movies = {}
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {
                        'year': row['year'],
                        'rating': row['rating'],
                        'poster': row['poster']
                    }
        except FileNotFoundError:
            pass
        return movies

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster):
        self.movies[title] = {
            'year': year,
            'rating': rating,
            'poster': poster
        }
        self.save_movies()

    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self.save_movies()

    def update_movie(self, title, rating):
        if title in self.movies:
            self.movies[title]['rating'] = rating
            self.save_movies()

    def save_movies(self):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, movie in self.movies.items():
                writer.writerow({
                    'title': title,
                    'year': movie['year'],
                    'rating': movie['rating'],
                    'poster': movie['poster']
                })