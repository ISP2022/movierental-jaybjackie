import logging
from typing import Collection
from price import PriceCode

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = PriceCode.REGULAR_PRICE
    NEW_RELEASE = PriceCode.NEW_RELEASE
    CHILDRENS = PriceCode.CHILDREN_PRICE
    
    def __init__(self, title: str, year: int, genre: Collection[str]):
        # Initialize a new movie. 
        self.title = title
        self.year = year
        self.genre = genre
    
    def get_title(self) -> str:
        return self.title

    def is_genre(self, string: str) -> bool:
        return any(g.lower() == string.lower() for g in self.genre)

    def __str__(self):
        return f"{self.title}({self.year})"
