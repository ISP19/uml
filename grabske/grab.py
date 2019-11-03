"""For choose the product and bring it to basket, and waiting for confirm order to buy"""

class Product:
    """class for object product that tells the name of product and price"""
    def __init__(self, product, price):
        self.product = product
        self.price = price

class Basket:
    """class of basket that collect the order that you need and use to confirm the order """
    def __init__(self, order): #order is productlist
        self.baskets = order

    def show_product(self):
        """To show the product in your basket"""
        return self.baskets

    def get_product(self):
        """to see each product"""
        product = []
        for i in self.baskets:
            product.append(i.product)
        return product

    def get_price(self):
        """to see each price"""
        total_price = 0
        for i in self.baskets:
            total_price += i.price
        return total_price

    def buy_order(self):
        """to confirm the order in your basket"""
        return f"your order is {self.get_product}, total price is {self.get_price}"
