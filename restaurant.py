class Restaurant():
	"""Model for a generic restaurant"""
	def __init__(self, name, cusine, number):
		self.name = name
		self.cusine = cusine
		self.number_served = 0

	def describe_restaurant(self):
		print(self.name + " is a " + self.cusine + " restaurant.")

	def open_restaurant(self):
		print(self.name + " is now open")

	def set_number_served(self, served):
		self.number_served += served

first = Restaurant('chillis', 'texmex',0)
second = Restaurant('carinos', 'itallian',0)
third = Restaurant('deli', 'sandwiches', 0)

first.describe_restaurant()
first.open_restaurant()

second.describe_restaurant()
second.open_restaurant()

print(third.number_served)
third.describe_restaurant()
third.set_number_served(3)
print(third.number_served)


