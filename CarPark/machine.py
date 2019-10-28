
class CarParking:
    def __init__(self, floor:int, capacity:int):
        self.floor = floor
        self.valid = capacity
        self.park = []

class Person:
    def __init__(self, name:str,age:int):
        self.name = name
        self.age = age
        
class Car:
    def __init__(self, brand:str,owner:Person,mile):
        self.brand = brand
        self.owner = owner
        self.miles = mile
    
    def park(self, carpark:CarParking):
        if carpark.valid >0:
            carpark.valid -= 1
            carpark.park.append(self)

class Toyota(Car):
    def __init__(self, model:str,owner:Person,mile:int):
        self.model = model 
        super().__init__('Toyota',owner,mile)

class Benz(Car):
    def __init__(self, model:str,owner:Person,mile:int):
        self.model = model 
        super().__init__('Benz',owner,mile)

house = CarParking(10,100)
korn = Person('korn',19)

korn_car = Benz('s350e',korn,0)
korn_car.park(house)
print(house.valid)



