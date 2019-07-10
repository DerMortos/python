filename = "text_files/guest_book.txt"
prompt = "Please enter your name: "

with open(filename, 'a') as file_object:
	guests = True
	while guests:
		message = input(prompt)

		if message == 'quit':
			active = False
		else:
			file_object.write(message + '\n')