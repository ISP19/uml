
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
    def __init__(self, brand:str,owner:Person):
        self.brand = brand
        self.owner = owner
    
    def park(self, carpark:CarParking):
        if carpark.valid >0:
            carpark.valid -= 1
            carpark.park.append(self)


house = CarParking(10,100)
korn = Person('korn',19)

car = Car('benz',korn)
car.park(house)
print(house.valid)



