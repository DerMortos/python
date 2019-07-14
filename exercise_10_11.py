import json

def get_new_number():
	"""find out users favorite number"""
	filename ='text_files/favorite_number.json'
	number = input("What is your favorite number?: ")
	with open(filename, 'w') as f_obj:
		json.dump(number, f_obj)
	return number

def load_stored_number():
	"""load users favorite number"""
	filename = 'text_files/favorite_number.json'
	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number
def fave_number():
	"""display favorite number"""
	number = load_stored_number()
	if number:
		print("Your favorite number is " + str(number))
	else:
		number = get_new_number()

fave_number()