"""
CS50 task 0.5
Complete tip calculator program.
"""


def main():
	dollars = dollars_to_float("How much was the meal? ")
	percent = percent_to_float("What percentage would you like to tip? ")
	tip = dollars * percent
	print(f"Leave ${tip:.2f}")


def dollars_to_float(prompt: str) -> float:
	while True:
		try:
			return float(
				input(prompt).strip("$").replace(
					",", "."
				)
			)
		except ValueError:
			print("Incorrect input.")


def percent_to_float(prompt: str) -> float:
	while True:
		try:
			return float(input(prompt).strip("%")) / 100
		except ValueError:
			print("Incorrect input.")


if __name__ == "__main__":
	main()
