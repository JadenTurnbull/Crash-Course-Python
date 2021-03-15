#2-10
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "               ada"
last_name = "lovelace"
full_name = f"{first_name.strip()} {last_name}"
print(full_name.title())

print(f"Hello, {full_name.title()}!")
print(f"\tHello, \n{full_name.title()}!")
print(f"Languages: \n\tPython \n\tC \n\tJavascript" )

print(0.04 + 0.01)

#more than one varaible
x, y, z = 0, 'one', 2
print(f"{x} {y} {z}")

#constant var
MAX_CONNECTIONS = 5000