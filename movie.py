import logging
from price import PriceStrategy

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title

    def get_price(self, days) -> float:
        amount = 0
        if self.get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 per day.
            amount = 2.0
            if days > 2:
                amount += 1.5*(days-2)
        elif self.get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 per day.
            amount = 1.5
            if days > 3:
                amount += 1.5*(days-3)
        elif self.get_price_code() == Movie.NEW_RELEASE:
            # Straight $3 per day charge
            amount = 3*days
        else:
            log = logging.getLogger()
            log.error(f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
        return amount
    
    def get_rental_points(self, days):
        if self.get_price_code() == Movie.NEW_RELEASE:
            # New release earns 1 point per day rented
            return days
        else:
            return 1

    def __str__(self):
        return self.title
