"""this file is for writing uml diagram about """
class Restuarant:
    """ function represent table and customer"""
    def __init__(self, table, customer):
        self.table = table
        self.customer = customer
class Customer:
    """ check customer"""
    def __init__(self, customer: int):
        self.customer = customer

class Table:
    """ class check for table and customer"""
    def __init__(self, chair: int):
        self.chair = chair
        self.list = []

    def apped_customer(self, customer: Customer):
        """append customer"""
        self.list.append(customer)

    def check_chair(self, customer: Customer)->bool:
        """check for empty chair"""
        if customer.customer >= self.chair:
            return False
        return True
