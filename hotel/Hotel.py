class Hotel:
    """Hotel management"""

    def __init__(self, name: str, city: str, phone_number: str, room: dict):
        """
        base variable
        """
        self.name = name
        self.city = city
        self.phone_number = phone_number
        self.room = room


    def booking(self, customer, room):
        """For booking the room using Customer and Room."""
        self.room[room] = customer
        return True

    def service_mange(self, room, service):
        """Manaing the service in hotel , booking service for customer."""
        self.room[room] = service
        return True


class Customer:
    """Customer information"""

    def __init__(self, name: str, surname: str, phone_number: str):
        """
        base variable
        """
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.requirement = "None"
        self.cash = 0

    def add_requirement(self, requirement):
        """Add special requirement"""
        self.requirement = requirement
        return self.requirement

    def cash_sum(self, room):
        """calculate cash for each customer"""
        self.cash = room.price
        return self.cash


class Room:
    """Room management"""

    def __init__(self, room_no: str, customer: Customer, day: int, price: int):
        """
        base variable
        """
        self.room_no = room_no
        self.customer = customer
        self.status = False
        self.day = day
        self.price = price


    def check_status(self):
        """
        Given the status for each room if room is availible return True and
        room is reserved return False
        """
        return self.status

    def check_price(self):
        """Given the price for each room reservation followed by their booking's day"""
        return self.day*self.price


class Service:
    """Service Management"""

    def __init__(self, name, price):
        """
        base variable
        """
        self.name = name
        self.price = price
        self.status = True
        self.payment = False

    def check_status(self):
        """
        Given the status for each service if service is availible return True and
        service is reserved return False
        """
        return self.status

    def check_payment(self):
        """return payment status for each service"""
        return self.payment
