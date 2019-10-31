class Restaurant:
	"""Class represents a point in cartesian coordinates"""
	def __init__(self,food:str,beverage:str,dessert:str, price:int,amount:int):
		self.food = food
		self.beverage = beverage
		self.dessert = dessert
		self.price = price
		self.amount = amount

class Price:
	def __init__(self, price): 
		self.price = price

	def sale(self) -> int:
		"""promotion of food,beverage,dessert"""
		return 50

class Food(Price):

	def __init__(self, price:int,amount)
		friedrice = Price(price)
		noodles = Price(price)
		self.amount = amount
		super().__init__([friedrice,noodles])

	def sale(self) -> int:
		return  (self.price * self.amount ) - Price.sale

class Beverage(Price):
	def __init__(self,beverage,price:int,amount):
		juice = Price(price)
		water = Price(price)
		self.amount = amount
		super().__init__([juice,water])

	def sale(self) -> int:
		return  (self.price * self.amount ) - Price.sale

class Dessert(Price):
	def __init__(self,dessert,price:int,amount):
		cake = Price(price)
		bread = Price(price)
		self.amount = amount
		super().__init__([cake,bread])

	def sale(self) -> int:
		return  (self.price * self.amount ) - Price.sale


	
	
