#5-8
users = ['admin', 'jeff', 'jayce', 'john', 'jme']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user} thank you for logging in')

#5-9
#Can't get else to show
users = []

if users:
    for user in users:
        print(f" Hello {user} thank you for logging in.")
    else:
        print("We need more users")

#5-10
current_users = ['Bwipo', 'Selfmade', 'Nisqy', 'Upset', 'Hyllisang']

new_users = ['Bwipo', 'Broxah', 'Caps', 'Rekkles', 'Hyllisang']

for user in new_users:
    if user in current_users:
        print("Sorry, username already taken")
    else:
        print(f"Username is availbale")

#5-11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
