from ast import arg
import csv
from movie import Movie

class MovieCatalog:

    def __init__(self):
        with open('movies.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            data = list(reader)[2:]
            for line in data:
                line[-1] = line[-1].split("|")
        self.movie_data = data

    def get_movie(self, *args):
        """Return list of movie information."""
        tmp = [line for line in self.movie_data if isinstance(args[0], str) and args[0] in line[1]]
        for movie in tmp:
            if args[0] in movie:
                if len(args) == 1:
                    return max(tmp)
                if str(args[1]) == movie[2]:
                    return movie
            
if __name__ == "__main__":
    catalog = MovieCatalog()
    movie = catalog.get_movie("No Time to Die")
    print(movie)