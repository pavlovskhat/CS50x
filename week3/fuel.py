"""
CS50 task4.1
Converting fractions to percentages.
Exception handling included.
"""


def get_fraction(prompt: str) -> int:
    while True:
        try:
            fraction = input(prompt)
            if "/" in fraction:
                return get_percentage(fraction.split("/"))
            else:
                print("Incorrect format.")
        except (ValueError, IndexError, ZeroDivisionError):
            print("Invalid input.")


def get_percentage(fraction: list) -> int:
    return int((int(fraction[0]) / int(fraction[1])) * 100)


def main():
    percentage = get_fraction("Fraction: ")
    if 1 < percentage < 99:
        print(f"{percentage}%")
    elif percentage <= 1:
        print("E")
    else:
        print("F")


if __name__ == "__main__":
    main()
