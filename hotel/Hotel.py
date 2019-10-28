class Hotel :
    def __init__(self,name,city,phone_number) :
        self.name = name
        self.street = street
        self.city = city
        self.phone_number = phone_number

    def booking(self,customer,room) :
        pass

    def service_mange(self,service,customer) :
        pass

    
class Customer :
    def __init__(self,name,surname,phone_number) :
        self.name = name
        self.surname = surname
        self.phone_number = phone_number


class Room :
    def __init__(self, room_no, customer):
        self.room_no = room_no
        self.customer = Customer(customer)


class Service :
    def __init__(self, name, price):
        self.name = name
        self.price = price

