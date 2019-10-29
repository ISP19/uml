class CottonCandy:
    def __init__(self, size, amount):
        self.size = size
        self.amount = amount
        self.price = 0

    def flavors(self):
        flavors = {'s':25, 'm':35, 'l':50}
        self.price = flavors.get(self.size)*self.amount

class Lollipop:
    def __init__(self, size, amount):
        self.size = size
        self.amount = amount
        self.price = 0

    def flavors(self):
        flavors = {'s':25, 'm':35, 'l':50}
        self.price = flavors.get(self.size)*self.amount


class CandyShop:
    def __init__(self, cottoncandy, lollipop):


        
