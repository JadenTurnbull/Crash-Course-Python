#4-15

#1
buffet = ('eggs', 'bacon', 'toast', 'muffin', 'sausage')
for food in buffet:
    print(food)

#2
pizzas = ['tangy russain', 'avo and feta', 'spare rib']

friend_pizzas = ['tangy russain', 'avo and feta', 'spare rib']

pizzas.append('supreme')

friend_pizzas.append('tropical')

for my_pizza in pizzas:
    print(f"My pizza's are {my_pizza}")

for friend_pizza in friend_pizzas:
    print(f"My friend's pizza's are {friend_pizza}")

#3
odd_numbers = range(1,20,2)
for number in odd_numbers:
    print(number)

#4
table_of_three = range(3, 31, 3)
for number in table_of_three:
    print(number)

