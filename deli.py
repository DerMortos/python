sandwhich_orders = ['reuben', 'blt', 'pastrami', 'tuna', 'egg', 'avocado',]
finished_sandwiches = []

while sandwhich_orders:
	current_sandwich = sandwhich_orders.pop()

	print("I mada a " + current_sandwich + ' sandwich.')
	finished_sandwiches.append(current_sandwich)

print("\nSandwiches made today:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)
