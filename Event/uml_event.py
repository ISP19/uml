""" Event """
class Address:
    """
    Collect the address of the event.
    """
    def __init__(self, district, subdistrict, province, postalcode):
        self.district = district
        self.subdistrict = subdistrict
        self.province = province
        self.postalcode = postalcode

    def __str__(self):
        return "Address"

    def get_address(self):
        """
        address
        """
        return self

class Contact:
    """
    Collect the contact information of an event organizer.
    """
    def __init__(self, number, email):
        self.number = number
        self.email = email

    def __str__(self):
        return "Number: " + self.number + " " + "Email: " + self.email

    def get_number(self):
        """
        number
        """
        return self.number

class Person:
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender

    def get_firstname(self):
        """
        firstname
        """
        return self.firstname

class Activity:
    def __init__(self, name, address: Address, contact: Contact, person: Person):
        self.name = name
        self.address = address
        self.contact = contact
        self.person = person

    def __str__(self):
        return self.name

class Event:
    def __init__(self, activity: Activity):
        self.activity = activity

    def __str__(self):
        return "Activity"

