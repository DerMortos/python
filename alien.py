# Make an empty list for storing aliens.
aliens = []

#make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#Show the firs 5 aliens
for alien in aliens[:5]:
	print(alien)
print('...')

#show how many alieens have been created.
print("Total number or aliens: " + str(len(aliens)))

something

