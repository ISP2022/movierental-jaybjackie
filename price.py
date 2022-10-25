from abc import ABC, abstractmethod

class PriceStrategy(ABC):
    """Abstract base class (interface) for rental pricing."""

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals get 1 point per day rented."""
        return days
    
    def get_price(self, days):
        return 3.0 * days

class RegularPrice(PriceStrategy):

    def get_rental_points(self, days):
        return 1

    def get_price(self, days):
        return 1.5 + (1.5*(days-2)) if days > 2 else 1.5

class ChildrensPrice(PriceStrategy):

    def get_rental_points(self, days):
        return 1
        
    def get_price(self, days):
        return 1.5 + (1.5*(days-2)) if days > 3 else 1.5

NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN =ChildrensPrice()