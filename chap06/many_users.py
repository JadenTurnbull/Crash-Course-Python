users = {
'aeinstein': {
			'first': 'albert',
			'last': 'einstein',
			'location': 'princeton',
},
'mcurie': {
			'first': 'marie',
			'last': 'curie',
			'location': 'paris',
},
}
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

cars = { 
	'bmw': {
		'color' : 'black',
		'doors' : '5',
		'size' : 'medium to large',
	},

	'mini': {
		'color' : 'white',
		'doors' : '4',
		'size' : 'small',
	},

	'isuzu': {
		'color' : 'silver',
		'doors' : '2',
		'size' : 'largish',
	}
}

for car, car_specs in cars.items():
	print(f"\nCar: {car}")
	car_color = f"{car_specs['color']}"
	total_doors = f"{car_specs['doors']}"
	car_size = f" {car_specs['size']}"

	print(f"\tCar color is : {car_color.title()}")
	print(f"\tCar has : {total_doors} doors")
	print(f"\tThe car is : {car_size.title()}")