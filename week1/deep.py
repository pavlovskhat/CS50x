"""
CS50 task1.1
Checking values.
"""


def check_42(value: str) -> str:
	return value.replace("-", " ").lower()


def main():
	question = check_42(input(
		"What is the Answer to the Great Question of Life, the Universe, and Everything?"
	))
	if question == "42" or question == "forty two":
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
