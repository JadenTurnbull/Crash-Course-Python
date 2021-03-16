#7-4

topping = ''

while True:
	prompt = 'What toppings do you want? '
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"{topping} has been added on your pizza!")

#7-5

age = ''

prompt = "How old are you?"
age = int(input(prompt))

if age <= 3:
	print("Ticket is free")
elif (age > 3) and (age < 12): 
	print("ticket is $10")
elif (age >= 12):
	print("ticket is $12")

#7-6

topping = ''

while True:
	prompt = 'What toppings do you want? '
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(f"{topping} has been added on your pizza!")

topping = ''
active = True

while active:
	prompt = 'What toppings do you want? '
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print(f"{topping} has been added on your pizza!")

topping = ''
active = True

while topping != 'quit':
	prompt = 'What toppings do you want? '
	topping = input(prompt)
	print(f"{topping} has been added on your pizza!")

#7-7

x = 1
while x <= 5:
print(x)


	