class Student:
    def __init__(self,x,y:int):
        self.name = x
        self.number = y
    def ConstraintAge(self,age):
        self.age = age
        if age >= 18:
            return True
class Course:
    def __init__(self,name,id,seats):
        self.name = name
        self.id = id
        self.seats = seats
class Seats:
    def __init__(self,seats:int,y):
        self.seats = seats
    def AvailableSeat(self,seats,y):
        return y - self.seats
