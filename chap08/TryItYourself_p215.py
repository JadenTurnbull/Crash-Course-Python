#8-12
'''
def sandwich(*fillings):
	print(f"\nFillings added: {fillings}")

sandwich('cheese', 'beef patty', 'tomato')
sandwich('ketchup', 'chicken', 'bacon', 'lettuce')
sandwich('bbq sauce', 'ribs')
'''
#8-13
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Jaden', 'Turnbull',
							location='Pretoria',
							field='IT',
							age= '18')

print(user_profile)

#8-14
def make_car(manufacturer, model, **car_info):
	car_info['brand'] = manufacturer
	car_info['model'] = model
	return car_info

complete_car = make_car('bmw', 'i8',
						color='black',
						electric='yes')

print(complete_car)
