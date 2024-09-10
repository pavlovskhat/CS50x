"""
CS50 task 1.5
Time conditional checks.
"""


def convert(time: str) -> float:
	return float(f"{time.split(":")[0]}.{time.split(":")[1]}")


def main():
	user_time = input("Enter time (hh:mm): ")
	if len(user_time.split(":")) == 2:
		if user_time.split(":")[0].isdigit() and user_time.split(":")[1].isdigit():
			if 7 <= convert(user_time) <= 8:
				print("breakfast time")
			elif 12 <= convert(user_time) <= 13:
				print("lunch time")
			elif 18 <= convert(user_time) <= 19:
				print("dinner time")
		else:
			print("Invalid time.")
	else:
		print("Invalid format.")


if __name__ == '__main__':
	main()
