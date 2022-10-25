from enum import Enum

class PriceCode(Enum):

    NEW_RELEASE = {"price": lambda days: 3.0*days, 
                    "frp": lambda days: days
                  }
    REGULAR_PRICE = {"price": lambda days: 2 + (1.5*(days-2)) if (days > 2) else 2,
                    "frp": lambda days : 1}
    CHILDREN_PRICE = {"price": lambda days: 1.5 + (1.5*(days-3)) if (days > 3) else 1.5,
                    "frp": lambda days : 1}

    def get_price(self, days: int) -> float:
        pricing = self.value["price"]
        return pricing(days)

    def get_rental_points(self, days: int) -> int: 
        rental = self.value['frp']
        return rental(days)