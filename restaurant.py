class Restaurant():
	"""Model for a generic restaurant"""
	def __init__(self, name, cusine):
		self.name = name
		self.cusine = cusine

	def describe_restaurant(self):
		print(self.name + " is a " + self.cusine + " restaurant.")

	def open_restaurant(self):
		print(self.name + " is now open")

first = Restaurant('chillis', 'texmex')
second = Restaurant('carinos', 'itallian')

first.describe_restaurant()
first.open_restaurant()

second.describe_restaurant()
second.open_restaurant()
