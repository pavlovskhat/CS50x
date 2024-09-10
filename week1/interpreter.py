"""
CS50 task1.4
Calculator application.
"""


def addition(a: int, b: int) -> int:
	return a + b


def subtraction(a: int, b: int) -> int:
	return a - b


def multiplication(a: int, b: int) -> int:
	return a * b


def division(a: int, b: int) -> int:
	try:
		return int(a / b)
	except ZeroDivisionError:
		return 0


def main():
	operations = [
		"+",
		"-",
		"/",
		"*"
	]
	equation = input("What is the equation? ")
	if len(equation.split()) == 3:
		if equation.split()[1] in operations:
			if equation.split()[0].isdigit() and equation.split()[2].isdigit():
				try:
					match equation.split()[1]:
						case "+":
							print(addition(
								int(equation.split()[0]),
								int(equation.split()[2])
							))
						case "-":
							print(subtraction(
								int(equation.split()[0]),
								int(equation.split()[2])
							))
						case "/":
							print(division(
								int(equation.split()[0]),
								int(equation.split()[2])
							))
						case "*":
							print(multiplication(
								int(equation.split()[0]),
								int(equation.split()[2])
							))
				except (ValueError, IndexError):
					print("Invalid input.")
			else:
				print("Invalid number.")
		else:
			print("Invalid operator")
	else:
		print("Invalid input.")


if __name__ == "__main__":
	main()
