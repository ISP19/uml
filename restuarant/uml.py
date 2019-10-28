class Restuarant:
    def __init__(self, table, customer):
        self.table = table
        self.customer = customer
    
class Table:
    def __init__(self, chair:int):
        self.chair = chair
        self.list = []

    def apped_customer(self, Customer: Customer):
       self.list.append(Customer)
    
    def check_chair(self, Customer: Customer)->bool:
        if Customer.customer >= self.chair:
            return False
        else:
            return True 


class Customer:
    def __init__(self, customer:int ):
        self.customer = customer
 
