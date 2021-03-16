#6-1
person = {
'first_name' : 'Dilan',
'last_name' : 'Turnbull',
'age' : 15,
'city' : 'Pretoria'
}

for key, value in person.items():
	print(f"{key.title()}, {value}")

#6-2
fav_number = {
	'jeff' : 2,
	'james' : 6,
	'jen' : 9,
	'john' : 3,
	'jaden' : 4,
}

for person, number in fav_number.items():
	print(f"{person.title()}'s favourite number is {number}")

#6-3
glossary = {
	'list' : 'Lists are used to store multiple items in a single variable, lists are created using square brackets',
	'tuple' : 'Tuples are used to store multiple items in a single variable, a tuple is a collection which is ordered and unchangeable, tuples are written with round brackets.',
	'sets' : 'Sets are used to store multiple items in a single variable, a set is a collection which is both unordered and unindexed, sets are written with curly brackets ',
	'dictionaries' : 'Dictionaries are used to store data values in key:value pairs, a dictionary is a collection which is ordered, changeable and does not allow duplicates, Dictionaries are written with curly brackets, and have keys and values.',
	'continue' : 'With the continue statement we can stop the current iteration, and continue with the next',
}

word = glossary['list'].title()
print(f"Lists: \n{word}")

word = glossary['tuple'].title()
print(f"Tuple's : \n{word}")

word = glossary['sets'].title()
print(f"Sets: \n{word}")

word = glossary['dictionaries'].title()
print(f"dictionaries : \n{word}")

word = glossary['continue'].title()
print(f"continue's : \n{word}")