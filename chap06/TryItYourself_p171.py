#6-7

dillan = {
'first_name' : 'Dilan',
'last_name' : 'Turnbull',
'age' : 15,
'city' : 'Pretoria'
}

jeff = {
'first_name' : 'Jeff',
'last_name' : 'Smit',
'age' : 21,
'city' : 'London',
}

jen = {
	'first_name' : 'Jen',
	'last_name'  : 'du Preez',
	'age' : 18
 }


people = [dillan, jeff, jen]

for person in people:
	for key, value in person.items():
		print(f"{value}" ) 

#6-8
milo = {
	'kind' : 'dog',
	'owner' : 'john'
}

jd = {
	'kind' : 'parrot',
	'owner': 'jack'
}

garfield = {
	'kind' : 'cat',
	'owner': 'jess'
}

pets = [milo, jd, garfield]

for pet in pets:
	for key, value in pet.items():
		print(f"{value}")

#6-9
favourite_places = {
	'Jaden' : 'Finland',
	'Esma' : 'Croatia',
	'Jen' : 'Japan'
}

for person, place in favourite_places.items():
	print(f"{person} -> {place}")


#6-10
fav_number = {
	'jeff' :[ 2, 1], 
	'james' : [6, 4],
	'jen' : [9, 6],
	'john' : [3, 2],
	'jaden' : [4, 8]
}

for person, numbers in fav_number.items():
	print(f"\n{person.title()}'s favourite number is :")
	for number in numbers:
		print(f"\t{number}")

#6-11
cities = {
	'Pretoria' : { 'population' : 2_473_000,
					'country' : 'South Africa',
					'fact' : "Pretoria's main street, formerly know as Church Street (now called Stanza Bopape) is the longest urban street in South Africa"
					},
	"Jo'burg": {'population' : 5_783_000,
					'country' : 'South Africa',
					'fact' : 'Johannesburg is home to 10 million trees, which helps the city cope with greenhouse effects and also lowers the noise levels within the city.'
	},
	'Cape-Town': { 'population' : 4_618_000,
					'country' : 'South Africa',
					'fact' : 'Cape Town was appointed the best place in the world to visit by the New York Times in 2014' 
	}
}

for city, city_info in cities.items():
	print(f"\n{city}")
	city_pop = f"{city_info['population']}"
	city_country = f"{city_info['country']}"
	city_fact = f"{city_info['fact']}"

	print(f"\t{city_pop}")
	print(f"\t{city_country.title()}")
	print(f"\t{city_fact}")
#6-12
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



		
