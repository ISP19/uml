class Event:
    def __init__(self, activity : Activity):
        self.activity = activity

class Activity:
    def __init__(self, name , address : Address, contact : Contact, person : Person):
        self.name = name
        self.address = address
        self.contact = contact
        self.person = person
    
    def place_at(self):
        return self.address

    def call(self):
        return self.contact
    
    def participate(self):
        return self.client
    
class Address:
    def __init__(self, district, subDistrict, road, province, postalcode):
        self.district = district
        self.subDistrict = subDistrict
        self.road = road
        self.province = province
        self.postalcode = postalcode

class Contact:
    def __init__(self,number,email):
        self.number = number
        self.email = email
    
class Person:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender