"""
CS50 task2.1
Convert from camel case to snake case.
"""


def snake(phrase: str) -> str:
	char_list = list(phrase)
	for index, char in enumerate(char_list):
		if char.isupper():
			char_list[index] = char.lower()
			char_list.insert(index, "_")
	return "".join(char_list)


def main():
	user_response = input("Variable name (use camelCase): ")
	print(f"Camel case: {user_response}")
	print(f"Snake case: {snake(user_response)}")


if __name__ == '__main__':
	main()
