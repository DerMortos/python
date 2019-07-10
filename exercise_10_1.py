filename = 'text_files/learning_python.txt'

"""Prints contents once by reading and printing file"""
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

"""Prints contents once by looping over the file object"""
print('\n')

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
"""
Prints contents once by storing the lines in a list and 
working them outside the block
"""
print('\n')
with open(filename) as file_object:
	lines = file_object.readlines()

message = ''
for line in lines:
	message += line.rstrip() + "\n"

print(message)
print(message.replace('Python', 'C'))
