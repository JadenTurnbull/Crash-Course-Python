#7-1

question = "Rental car"
question += "\nWhat rental car do you want? "
car = input(question)
print(f"\nLet me see if we have a {car}")

#7-2    

prompt = "How many people are in your group?"
number = int(input(prompt))
if number >= 8:
	print("Sorry, you'll have to wait for a table")
else:
	print("You're table is ready")

#7-3
prompt = 'Give a number '
number = int(input(prompt))
if number % 10 == 0:
	print(f"\n{number} is a multiple of 10")
else:
	print(f"\n{number} is not a multiple of 10")