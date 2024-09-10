"""
CS50 task 0.4
Create E=mc2 equation.
Ask user for mass in kg.
"""


def get_float(prompt: str) -> float:
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a number.")


def get_energy(mass: float) -> float:
	return mass * (300000000 ** 2)


def main():
	print(f"E = {get_energy(get_float('Enter mass: '))} Joule")


if __name__ == '__main__':
	main()
