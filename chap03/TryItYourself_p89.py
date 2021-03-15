#3-4
geust_list = ['Adam Sandler', 'Jeff', 'Ryan Reynolds']

for geusts in geust_list:
	print(f"{geusts} you are invited")

#3-5
print(f"{geust_list[1]} can't make it")

geust_list.append('Chris')
for geusts in geust_list:
	print(f"{geusts} you are invited")	 

#3-6
geust_list.insert(0, 'Dillan')
geust_list.insert(3, 'Gabriel')
geust_list.append('Dono')

for geusts in geust_list:
	print(f"{geusts} you are invited")

#3-7
print("/n Can only invite two peeps")


removed_geusts = geust_list.pop()

