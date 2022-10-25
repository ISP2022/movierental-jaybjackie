from enum import Enum

class PriceStrategy(Enum):
    """Implement a Price Strategy using Enum."""
    NEW_RELEASE = {"price": lambda days: 3.0*days, 
                    "frp": lambda days: days
                  }
    REGULAR_PRICE = {"price":2, "frp": 1}
    CHILDREN_PRICE = {"price": 1.5, "frp": 1}
    
    def get_price(self, days: int) -> float:
        pricing = self.value["price"]
        return pricing(days)

    def get_rental_points(self, days: int):
        freq_rental_points = self.value["frp"]
        return freq_rental_points(days)
