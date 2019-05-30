#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is you first name? "

#name = input(prompt)
#print("Hello, " + name + '!')

def greet_user(username):
	"""Display a simple greeting"""
	print("Hello, " + username.title() + "!")

greet_user("jesse")