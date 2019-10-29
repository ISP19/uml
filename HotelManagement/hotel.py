class Customer:
    """Class"""
    def __init__(self, booking_id:string, room:Room, name:string, phone_number:string, billing:float):
        self.booking_id = booking_id
        self.room = room
        self.name = name
        self.phone_number = phone_number
        self.billing = billing

class Room:
    def __init__(self, room_no: int, floor: int):
        self.room = room
        self.floor = floor
    
    def stay(self):
        """test if customer is staying in that room"""
        # code omitted
        return True

class Receptionist():
    def __init__(self, desk_number):
        self.customer_list = [] #customer is a list of Customers
        self.desk_number = desk_number

    def book_room(self):
        # code omitted
        pass

    def cancel_booking(self):
        # code omitted
        pass

    def generate_bill(self):
        # code omitted
        pass