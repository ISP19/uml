class Person:
    def __init__(self,name,age,telephone):
        self.name=name
        self.age=age
        self.telephone=telephone
    
    def pick_up(self,person):
        print(f"{self.name} pick up {person}")

class Telephone:
    def __init__(self, brand,color,price,owner):
        self.brand = brand
        self.color = color
        self.price = price
        self.owner = owner

    def call(self,person):
        print(f"{self.owner} calling {person.name}")
        person.pick_up(self.owner)
    
    def take_a_picture(self,side):
        print(f"Open {side} camera")

class Student(Person):
    def __init__(self, name,age,telephone):
        super().__init__(name, age,telephone)
        self.duty = "Study"