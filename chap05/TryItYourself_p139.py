#5-3
alien_color = 'green'

if alien_color == 'green':
	print('You scored 10 points')

alien_color = 'red'

if alien_color == 'green':
	print("You scored 5 points")

#5-4
if alien_color == 'green':
	print("You scored 5 points")
else: 
	print("You scored 10 points")

#5-5
if alien_color == 'green':
	print("You scored 5 points")
elif alien_color == 'yellow':
	print("You scored 10 points")
elif alien_color == 'red':
	print("You scored 15 points")
else: 
	print("You scored 10 points")

#5-6
age = 5;

if age < 2:
	print('person is baby')
elif (age >= 2) and (age < 4):
	print("person is toddler")
elif (age >= 4) and (age < 13):
	print("person is kid")
elif (age >= 13) and (age < 20):
	print("person is teenager")
elif (age >= 20) and (age < 65):
	print("person is adult")
elif age >= 65:
	print("person is elder")

#5-7
fav_fruits = ['litchi', 'starfruit', 'watermelon']

for fruit in fav_fruits:
	if fruit == 'litchi':
		print("you really like litchi's")
	if fruit == 'apple':
		print("you really like apple's")
	if fruit == 'mango':
		print("you really like mangos")
	if fruit == 'starfruit':
		print("you really like starfruit")
	if fruit == 'banana':
		print("you really like banana's")


