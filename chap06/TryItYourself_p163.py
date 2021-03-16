#6-4
glossary = {
	'list' : 'Lists are used to store multiple items in a single variable, lists are created using square brackets',
	'tuple' : 'Tuples are used to store multiple items in a single variable, a tuple is a collection which is ordered and unchangeable, tuples are written with round brackets.',
	'sets' : 'Sets are used to store multiple items in a single variable, a set is a collection which is both unordered and unindexed, sets are written with curly brackets ',
	'dictionaries' : 'Dictionaries are used to store data values in key:value pairs, a dictionary is a collection which is ordered, changeable and does not allow duplicates, Dictionaries are written with curly brackets, and have keys and values.',
	'continue' : 'With the continue statement we can stop the current iteration, and continue with the next',
	'Key Function' : "It is a callable that returns a value that we can use for sorting or ordering. We also call it a collation function. Functions like max(), min(), and sorted() make use of them.",
	'Attribute' : 'An attribute is a value an object holds. We can access an object’s attributes using the dot operator (.).',
	'Python Function' : 'A function is a sequence of statements that may return a value to the caller. It may take zero or more arguments.',

}

for word, defenition in glossary.items():
	print(f"\t{word.title()} \n{defenition} ")

#6-5
rivers = {
	'Nile' : 'Tanzania',
	'Amazon' : 'Brazil',
	'Yangtze' : 'China',
}

for river in rivers:
	print(f"{river}")

for country in rivers:
	print(f"{country}")

#6-6
favourite_languages = {
 	'jen' : 'python',
 	'sarah': 'C',
 	'edward' : 'ruby',
 	'phill' : 'python'
	}

take_poll = ['jen', 'sarah', 'jeff', 'edward', 'james']

for people in take_poll:
	if people in favourite_languages:
		print(f"Thank you for completing the poll {people}")
	elif people not in favourite_languages:
		print(f"Please do the poll {people}")
