class Product:
    def __init__(self, product, price):
        self.product = product

class Basket:
    def __init__(self, order): #order is productlist
        self.baskets = order

    def show_product(self):
        return self.baskets

    def get_product(self):
        product = []
        for i in self.baskets:
            product.append(i.product)
        return product

    def get_price(self):
        total_price = 0
        for i in self.baskets:
            total_price += i.price    
        return total_price


    def buy_order(self):
        return f"your order is {self.get_product}, total price is {self.get_price}"