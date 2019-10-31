"""This code shows hotel management"""
class Customer:
    """This class collect information on the customers"""
    def __init__(self, booking_id: str, name: str, billing: float):
        self.booking_id = booking_id
        self.name = name
        self.billing = billing

    def request_room_service(self):
        """This meathod is use when cutomer wants to use room service"""
        # code omitted

    def request_room(self):
        """This meathod is use to check if the room is available"""
        # code omitted

class Room:
    """Informations on room"""
    def __init__(self, room_no: int, floor: int, customer: Customer):
        self.room = room_no
        self.floor = floor
        self.status = True

    def check_staying(self):
        """test if customer is staying in that room"""
        # code omitted

class Receptionist:
    """This class is use when customer books, or cancel a room"""
    def __init__(self, desk_number):
        self.desk_number = desk_number
        self.room_list = []

    def book_room(self, customer, room_no):
        """This meathod is use when customer books a room"""
        # code omitted

    def cancel_booking(self, customer, room_no):
        """This meathod is use to delete information on customer booking"""
        # code omitted

    def generate_bill(self, room):
        """This meathod calculates the bill for each customers"""
        # code omitted
