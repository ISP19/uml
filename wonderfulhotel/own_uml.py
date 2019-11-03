class Toilet:
    """Toilet class"""
    def __init__(self, numbertoilet):
        self.numbertoilet = numbertoilet

class Bedroom():
    """Bedroom class"""
    def __init__(self, roomnumber):
        self.roomnumber = roomnumber
        self.toilet = []

    def add_toilet(self, toilet: Toilet):
        """add toilet to bedroom"""
        self.toilet.append(toilet)

class Customer:
    """Customer class"""
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_customer(self):
        """get customer from everywhere"""
        # code omitted

class Hotel:
    """Hotel class"""
    def __init__(self):
        self.customers = []
        self.bedrooms = []

    def add_customer(self, customer: Customer):
        """add customer in hotel"""
        self.customers.append(customer)

    def add_room(self, bedroom: Bedroom):
        """add room in hotel"""
        self.bedrooms.append(bedroom)
