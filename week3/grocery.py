"""
CS50 task4.3
Shopping list widget.
"""
from operator import itemgetter


def view_shopping(data: dict):
    keys = sorted(data, key=itemgetter(0))
    for key in keys:
        print(f"{data[key]}: {key.upper()}")


def main():
    shopping_list = {}
    while True:
        item = input("Item or '0' to exit: ")
        if item in shopping_list:
            shopping_list[item] += 1
        elif item == "0":
            exit("Goodbye")
        else:
            shopping_list[item] = 1
        view_shopping(shopping_list)


if __name__ == "__main__":
    main()
