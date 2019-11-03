
class Concert:
    """Class of concert information"""
    def __init__(self, title: str, username: str, price: int, seat: int):
        self.title = title
        self.username = username
        self.price = price
        self.seat = seat


class Customer:
    """Class represents customer information"""
    def __init__(self, name: str, surname: str, username: str):
        self.name = name
        self.surname = surname
        self.username = username


class Reserve(Concert):
    """Class represents detail of reserve"""
    def __init__(self):
        self.detail = []
        self.status = False

    def add_detail(self, customer=Customer):
        """

             Add detail of customer

        """
        self.detail.append(customer)

    def total_price(self):
        """

              Calculate the total price

        """
        return self.price * self.seat

    def check_username(self):
        """
              check username of customer and concert class if they are the same return
              True and if they are not the same return False
        """
        # code omitted
        return self.status

    def __str__(self):
        """
               Display the detail of reserve

        """
        # code omitted
        check = self.check_username
        seat = self.seat
        price = self.price
        username = self.username
        title = self.title
        total = self.total_price()
        if check and isinstance(check, True):
            return f"{username} reserves {title} concert \n" \
                   f"seat(s): {seat} \nprice : {price} \nTotal: {total}"
        return "Your usename is incorrect"