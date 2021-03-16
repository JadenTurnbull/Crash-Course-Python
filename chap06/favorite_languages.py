favourite_languages = {
 	'jen' : 'python',
 	'sarah': 'C',
 	'edward' : 'ruby',
 	'phill' : 'python'
	}

language = favourite_languages['jen'].title()
print(f"Jen's favourite language is {language}.")

language2 = favourite_languages.get('jeff','No point value assigned')
print(language2)

for key, value in favourite_languages.items():
	print(f"Key: {key.title()} Value: {value}")

print('Accessing keys')
for key in favourite_languages.keys():
	print(f"Key: {key.title()}")

print('Accessing values')
for value in favourite_languages.values():
	print(f"Values: {value.title()}")

fav_cars = {
 	'jeff' : 'bmw',
 	'jayce' : 'audi',
 	'george' : 'mini'
 }

for key, value in fav_cars.items():
 	print(f"Key is: {key.title()} Value is: {value}")

print('Keys')
for key in fav_cars.keys():
 	print(f"Key is: {key.title()}")	

print('Value')
for value in fav_cars.values():
 	print(f"Value is: {value.title()}")	


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")