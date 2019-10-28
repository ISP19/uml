
class CottonCandy:
    def __init__(self, size, amount):
        self.size = size
        self.amount = amount
        self.price = 0

    def flavors(self):
        flavors = {'s':25, 'm':35, 'l':50}
        self.price = flavors.get(self.size)*self.amount
        return self.price

class Lollipop:
    def __init__(self, size, amount):
        self.size = size
        self.amount = amount
        self.price = 0

    def flavors(self):
        flavors = {'s':30, 'm':40, 'l':50}
        self.price = flavors.get(self.size)*self.amount
        return self.price

class CandyShop:
    def __init__(self, candy, size, amount):
        self.candy = candy
        self.size = size
        self.amount = amount
    
    def payment(self):
        if self.candy == 1:
            CottonCandy(self.size, self.amount)
        elif self.candy == 2:
            Lollipop(self.size, self.amount)



        

        
