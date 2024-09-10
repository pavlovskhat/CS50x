"""
CS50 task2.4
Validate string pattern.
"""


def scan_pattern(string: str) -> bool:
	first_digit = False
	for char in string:
		if char.isdigit():
			if not first_digit and char == "0":
				return False
			else:
				first_digit = True
		elif char.isalpha():
			if first_digit:
				return False
		else:
			return False
	return True


def is_valid(string: str) -> bool:
	if 2 <= len(string) <= 6:
		return scan_pattern(string)
	else:
		return False


def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")


if __name__ == "__main__":
	main()
