

class Concert:
    def __init__(self, username: str, price: int, seat: str):
        self.username = username
        self.price = price
        self.seat = seat


class Customer:
    def __init__(self, name: str, surname: str, username: str):
        self.name = name
        self.surname = surname
        self.username = username


class Reserve(Concert):
    def __init__(self):
        self.detail = []

    def add_detail(self, customer=Customer):
        self.detail.append(customer)

    def total_price(self):
        return self.price * self.seat

    def check_id(self):
        pass

    def __str__(self):
        pass
