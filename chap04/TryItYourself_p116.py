#4-10
cars = ['bmw', 'audi', 'mercedes', 'mini', 'toyota', 'kia', 'ford', 'nissan', 'buggatti']
print(f"The first three items in the list are {cars[0:3]}")

print(f"Three items from the middle of the list are {cars[3:6]}")

print(f"The last three items in the list are {cars[6:9]}")

#4-11
pizzas = ['tangy russain', 'avo and feta', 'spare rib']

friend_pizzas = ['tangy russain', 'avo and feta', 'spare rib']

pizzas.append('supreme')

friend_pizzas.append('tropical')

for my_pizza in pizzas:
	print(f"My pizza's are {my_pizza}")

for friend_pizza in friend_pizzas:
	print(f"My friend's pizza's are {friend_pizza}")

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

for my_food in my_foods:
	print(f"My foods are {my_food}")

for fr_food in friend_foods:
	print(f"My foods are {fr_food}")