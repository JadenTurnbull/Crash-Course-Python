bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])

motorcycles = ['honda', 'suzuki', 'yamaha']
print(motorcycles)
motorcycles.append('ducati')
motorcycles.insert(1, 'bmw')
print(motorcycles)

del motorcycles[0]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#first_owned = motorcycles.pop(0)
#print(f"The first motorcycle I owned was a {first_owned.title()}.")

too_expensive = 'bmw'
motorcycles.remove(too_expensive)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse= True)
print(cars)

cars.reverse()
print(cars)
print(len(cars))

print(cars[-1])