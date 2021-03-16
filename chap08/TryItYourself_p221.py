#8-15
def make_shirt(size, *colors):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a shirt with size {size} with the following color combinations:")
	for color in colors:
		print(f"- {color}")