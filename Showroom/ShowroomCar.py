class Price:
    """This class show a price and promotion."""
    def __init__(self, price):
        self.price = price

    def promotion_car(self) -> int:
        """special promotion of car's price for special customer and member in company"""
        return self.price*0.4

    def promotion_motorbike(self) -> int:
        """special promotion of motorbike's price for special customer and member in company"""
        return self.price*0.5

class Car(Price):
    """ This class represents a price and promotion of each car. """
    def __init__(self, price: int, amount):
        honda = Price(price)
        toyota = Price(price)
        self.amount = amount
        super().__init__([honda, toyota])

    def promotion(self) -> int:
        """special promotion for special customer and member in company"""
        return (self.price*self.amount) - Price.promotion_car

class Motorbike(Price):
    """ This class represents a price and promotion of each motorbike. """
    def __init__(self, price: int, amount):
        kawazaki = Price(price)
        yamaha = Price(price)
        self.amount = amount
        super().__init__([kawazaki, yamaha])

    def promotion(self) -> int:
        """special promotion for special customer and member in company"""
        return (self.price*self.amount) - Price.promotion_motorbike

class Showroom:
    """This class represents a type and price of each car."""
    def __init__(self, car: str, motorbike: str, price: int, speed_max: int):
        self.car = car
        self.motorbike = motorbike
        self.price = price
        self.speed_max = speed_max
