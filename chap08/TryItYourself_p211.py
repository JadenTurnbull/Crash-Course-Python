#8-9
def show_messages(msgs):
	for msg in msgs:
		text = f"{msg}"
		print(text)

messages = ['Hi there micheal', 'hehe lol xD', "G'day mate"]
show_messages(messages)

#8-10

def show_messages(msgs):
	for msg in msgs:
		text = f"{msg}"
		print(text)

sent_messages = []
messages = ['Hi there micheal', 'hehe lol xD', "G'day mate"]
show_messages(messages)
	


def send_messages():
		while messages:
			sent = messages.pop()
			print(f"Sending : {sent}")
			sent_messages.append(sent)

send_messages()

print(messages)
print(sent_messages)

#8-11

show_messages(messages[:])
		



