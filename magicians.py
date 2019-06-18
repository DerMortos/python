magicians = ['jerri', 'milton', 'sheila', 'pita']
magicians_upgrade = []

def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	while magicians:
		current_magician = magicians.pop() + ' the great'
		magicians_upgrade.append(current_magician)


show_magicians(magicians)
make_great(magicians[:])

print(magicians)
print(magicians_upgrade)