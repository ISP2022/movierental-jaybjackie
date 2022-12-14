# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from price import PriceCode
from rental import Rental
from customer import Customer

def make_movies():
    movies = [
        Movie("No Time to Die", Movie.NEW_RELEASE),
        Movie("CitizenFour", Movie.REGULAR),
        Movie("Frozen", Movie.CHILDRENS),
        Movie("Top Gun: Maverick", Movie.NEW_RELEASE),
        Movie("Particle Fever", Movie.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        price = PriceCode(Movie.get_price_code(movie))
        customer.add_rental(Rental(movie, days, price))
        days = (days + 2) % 5 + 1
    print(customer.statement())
