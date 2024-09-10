"""
CS50 task1.2
Checking values.
"""


def main():
	greeting = input("Greeting: ").lower()
	if greeting == "hello":
		print("$0")
	elif any(list(greeting)):
		if greeting[0] == "h":
			print("$20")
		else:
			print("$100")
	else:
		print("You did not enter a greeting.")


if __name__ == "__main__":
	main()
