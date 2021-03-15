#3-8
travel = ['Finland', 'Maldives', 'Mauritius', 'Iceland', 'Alaska']

for country in travel:
	print(f"{country}")



for country in travel:
	print(f"{sorted(travel)}")

print(travel)

print(sorted(travel, reverse = True))

print(travel)

travel.reverse()
print(travel)

travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse = True)
print(travel)

#3-9
geust_list = ['Adam Sandler', 'Jeff', 'Ryan Reynolds']

print(len(geust_list))

#3-10
cars = ['bmw', 'toyota', 'mercedes', 'audi', 'Mini']

print(cars)
print(cars[0])

print(cars)
cars.append('ducati')
cars.insert(1, 'bmw')
print(cars)

del cars[0]

print(cars)

popped_cars = cars.pop()
print(cars)
print(popped_cars)

first_owned = cars.pop(0)
print(f"The first car I owned was a {first_owned.title()}.")

too_expensive = 'audi'
cars.remove(too_expensive)

cars.sort(reverse= True)
print(cars)

cars.reverse()
print(cars)
print(len(cars))

print(cars[-1])
