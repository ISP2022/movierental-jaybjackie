import csv
from movie import Movie

class MovieCatalog:

    def __init__(self):
        self.movie_data = []
        with open('movies.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            data = list(reader)[2:]
            for line in data:
                line[-1] = line[-1].split("|")
            for line in data:
                movie = Movie(line[1], int(line[2]), line[-1])
                self.movie_data.append(movie)

    def get_movie(self, *args):
        """Return list of movie information."""
        tmp = []
        if isinstance(args[0], str):
            for movie in self.movie_data:
                if args[0] in movie.title:
                    tmp.append(movie)
            for movie in tmp:
                if args[0] in movie.title:
                    if len(args) == 1:
                        return max(m for m in tmp)
                    if args[1] == movie.year:
                        return movie

if __name__ == "__main__":
    catalog = MovieCatalog()
    movie = catalog.get_movie("No Time to Die")
    print(movie)
