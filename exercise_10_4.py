filename = "text_files/guest_book.txt"
prompt = "Please enter your name: "

with open(filename, 'a') as file_object:
	while True:
		message = input(prompt)

		if message == 'quit':
			break
		else:
			file_object.write(message + '\n')