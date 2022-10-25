import logging
from price import PriceCode

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = PriceCode.REGULAR_PRICE
    NEW_RELEASE = PriceCode.NEW_RELEASE
    CHILDRENS = PriceCode.CHILDREN_PRICE
    
    def __init__(self, title, price_code: PriceCode):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title

    def get_price(self, days: int) -> float:
        return self.price_code.get_price(days)
    
    def get_rental_points(self, days):
        return self.price_code.get_rental_points(days)


    def __str__(self):
        return self.title
