"""
CS50 task 0.3
Convert emojis to unicode.
"""


def convert(phrase: str) -> str:
	return phrase.replace(
		":)", "🙂"
	).replace(
		":(", "🙁"
	)


def main():
	print(convert(input("Enter a phrase: ")))


if __name__ == '__main__':
	main()
