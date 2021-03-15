#4-3
numbers = list(range(1,21))
print(numbers)

#4-4
numbers = list(range(1,1_000_001))
print(numbers)

#4-5
numbers = list(range(1,1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
odd_numbers = range(1,20,2)
for number in odd_numbers:
	print(number)

#4-7
table_of_three = range(3, 31, 3)
for number in table_of_three:
	print(number)

#4-8
cubes = [1**3, 2**3, 3**3, 4**3, 5**3, 6**3, 7**3, 8**3, 9**3, 10**3]
for cube in cubes:
	print(cube)

#4-9
cubes = [num**3 for num in range(1,11)]
print(cubes)