"""
CS50 task2.2
Slot machine that accepts coins
until 50c is paid in either 5, 10
or 25 denominations.
"""


def main():
	debt = 50
	accepted_coins = [
		25,
		10,
		5
	]
	print(f"Amount due: {debt}c")
	while True:
		user_deposit = int(input("Insert coin: "))
		if user_deposit in accepted_coins:
			debt -= user_deposit
		print(f"Amount due: {debt}c")
		if debt <= 0:
			break


if __name__ == '__main__':
	main()
