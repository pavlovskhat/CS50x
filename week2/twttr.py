"""
CS50 task2.3
Removes vowels from strings.
"""


def pop_vowels(string: str) -> str:
	vowels = [
		"a", "e", "i", "o", "u",
	]
	result = []
	for index, letter in enumerate(string):
		if letter not in vowels:
			result.append(letter)
	return "".join(result)


def main():
	print(pop_vowels(input(
		"Enter a string: "
	).lower()))


if __name__ == '__main__':
	main()
