class Showroom:
    def __init__(self, car:str, motorbike:str, price:int, speed_max:int):
        self.car = car
        self.motorbike = motorbike
        self.price = price
        self.speed_max = speed_max

class Price:
	def __init__(self, price): 
		self.price = price

	def promotion(self) -> int:
		"""special promotion for special customer and member in company"""
		return (self.price)*0.4

class Car(Price):

	def __init__(self, price:int,amount):
		self.honda = Price(price)
		self.toyota = Price(price)
		self.amount = amount
		super().__init__([honda,toyota])

	def promotion(self) -> int:
		return  (self.price * self.amount ) - Price.promotion

class Motorbike(Price):

    def __init__(self, price:int, amount):
        self.kawazaki = Price(price)
        self.yamaha = Price(price)
        self.amount = amount
		super().__init__([kawazaki,yamaha])
        