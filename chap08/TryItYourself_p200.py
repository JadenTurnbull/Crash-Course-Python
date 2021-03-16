#8-3

def make_shirt(size, text):
	print(f"The shirt's size is {size} and you want {text} written on it")

make_shirt('large', 'lol xD')

make_shirt(size = 'medium', text = 'lol xDs')

#8-4
def make_shirt(size = 'large', text = 'I love Python'):
	print(f"The shirt's size is {size} and you want {text} written on it")

make_shirt('large')

make_shirt('medium')

make_shirt('large', 'Python is cool')

#8-5

def describe_city(city, country = 'South Africa'):
	print(f"{city.title()} is in {country.title()}")

describe_city("jo'burg")
describe_city('cape town')
describe_city('sydney', 'australia')
