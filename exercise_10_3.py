filename = 'text_files/guest.txt'

with open(filename, 'a') as file_object:
	user = input("What is your name?: ")
	file_object.write(user + '\n')