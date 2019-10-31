class CarParking:
    """CarPark class"""
    def __init__(self, floor: int, capacity: int):
        self.floor = floor
        self.valid = capacity
        self.park = []

    def __str__(self):
        return f"floor {self.floor} valid for {self.valid}"

class Person:
    """ human class"""
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
    # def talk(word):
    #     """talk"""
    #     return f"{word}!!"
    def __str__(self):
        return f"{self.name} age {self.age} years old is {self.gender}"

class Car:
    """class car"""
    def __init__(self, brand: str, owner: Person, mile):
        self.brand = brand
        self.owner = owner
        self.miles = mile

    def park(self, carpark: CarParking):
        """parking method"""
        if carpark.valid > 0:
            carpark.valid -= 1
            carpark.park.append(self)

class Toyota(Car):
    """toyota brand  class inherit from Car class"""
    def __init__(self, model: str, owner: Person, mile: int):
        self.model = model
        super().__init__('Toyota', owner, mile)

class Benz(Car):
    """benz brand class inherit from car class"""
    def __init__(self, model: str, owner: Person, mile: int):
        self.model = model
        super().__init__('Benz', owner, mile)

# house = CarParking(10, 100)
# korn = Person('korn', 19, 'male')
# korn_car = Benz('s350e', korn, 0)
# korn_car.park(house)
# print(house.valid)
