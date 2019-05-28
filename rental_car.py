available_cars = ['compact', 'sedan', 'suv', 'truck',]

car = input("What kind of car would you like to rent? ")
if car in available_cars:
	print('Let me find you a nice ' + car + '.')
else:
	print("Sorry, we don't have any " + car + "s available. ")
	print("You can choose either: compact, sedan, suv or truck.")