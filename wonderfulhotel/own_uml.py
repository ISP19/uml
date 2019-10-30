class Hotel:
    def __init__ (self):
        self.customers = []
        self.bedrooms = []
    
    def add_customer(self, Customer):
        self.customers.append(Customer)
    
    def add_room(self, Bedroom):
        self.bedrooms.append(Bedroom)

class Bedroom():
    def __init__(self, roomnumber):
        self.roomnumber = roomnumber
        self.toilet = []
    
    def add_toilet(self, Toilet):
        self.toilet.append(Toilet)

class Toilet:
    def __init__(self,numbertoilet):
        self.numbertoilet = numbertoilet

class Customer:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    
