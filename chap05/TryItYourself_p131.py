#5-1
food = 'egg'
print("Is food == 'egg'? I predict True.")
print(food == 'egg')
print("\nIs food == 'bacon'? I predict False.")
print(food == 'bacon')

car = 'bmw'
print("Is car == 'bmw'? I predict True.")
print(car == 'bmw')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

bicycle = 'mountain'
print("Is bicycle == 'mountain'? I predict True.")
print(bicycle == 'mountain')
print("\nIs bicycle == 'trek'? I predict False.")
print(food == 'trek')

apple = 'red'
print("Is apple == 'red'? I predict True.")
print(apple == 'red')
print("\nIs apple == 'green'? I predict False.")
print(apple == 'green')

cheetah = 'fast'
print("Is cheetah == 'fast'? I predict True.")
print(cheetah == 'fast')
print("\nIs cheetah == 'slow'? I predict False.")
print(cheetah == 'slow')

#5-2
message = "The BMW is gold"
car = "BMW"

if car == message:
    print('strings equal')

fire = 'Hot'
fire.lower() == 'hot'

speed = 120

if speed >= 120:
	print("over the limit")

if speed <=120:
	print("safe")

number = 24

if number != 24:
	print("wrong sorry")

car = 'ford'
wheels = 'black'

if (car == 'ford') and (wheels == 'black'):
	print("nice")

if (car == "ford") or (wheels == "white"):
	print("cool")

cars = ['bmw', 'mini']
'mini' in cars

car = 'audi'

if car not in cars:
	print(f"{car} is not in list")



