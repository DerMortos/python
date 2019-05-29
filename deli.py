sandwich_orders = ['reuben', 'blt', 'pastrami', 'tuna', 'pastrami', 
						'egg', 'avocado', 'pastrami']
finished_sandwiches = []

print("Sorry, We have run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
		sandwich_orders.remove('pastrami')
		
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()


	print("I mada a " + current_sandwich + ' sandwich.')
	finished_sandwiches.append(current_sandwich)

print("\nSandwiches made today:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
