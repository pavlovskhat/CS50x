"""
CS50 task4.2
Mock restaurant order app.
Live order receipt.
Validation included.
"""
import json
from tabulate import tabulate


def import_json(file_path: str, mode="r") -> dict:
    """
    Imports JSON file as dictionary.

    :param file_path: File location.
    :param mode: Reading mode default.
    :return: Data dictionary.
    """
    with open(file_path, mode) as file:
        return json.load(file)


def format_menu_string(item_string: str, delim="_") -> str:
    """
    Replaces character with spaces and titles
    each word in the given string.

    :param item_string: Given string.
    :param delim: Underscore by default.
    :return: Formatted string.
    """
    return item_string.replace(delim, " ").title()


def view_menu(data: dict):
    """
    Displays data from dictionary in a
    readable format.

    :param data: Data dictionary.
    """
    for index, item in enumerate(data.items(), 1):
        print(f"{index}) {format_menu_string(item[0])}: ${item[1]:,.2f}")


def get_int(prompt: str) -> int:
    """
    Gets an integer from the user.

    :param prompt: Input instruction.
    :return: Valid integer.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Incorrect Choice")


def get_order(menu: dict, prompt: str) -> tuple:
    """
    Selects menu option from user input.
    Returns the selected key and value as
    a tuple.

    :param menu: Menu dictionary.
    :param prompt: Input instruction.
    :return: Key value tuple.
    """
    while True:
        menu_number = get_int(prompt)
        if len(menu) >= menu_number > 0:
            item = list(menu.keys())[menu_number - 1]
            return item, menu[item]
        elif menu_number == 0:
            exit("Goodbye")
        else:
            print("Incorrect Option")


def generate_total(data: dict) -> int:
    """
    Sums all the values of the given
    dictionary.

    :param data: Data dictionary.
    :return: Integer total.
    """
    return sum(value for value in data.values())


def generate_invoice(data: dict):
    """
    Prints tabled invoice view.

    :param data: Data dictionary.
    """
    if data:
        print(tabulate(data.items()))
        print(f"\033[1m${generate_total(data):,.2f}\033[0m")


def start_banner():
    """
    Prints program welcome banner.
    """
    print(f"{'='*50}")
    print("\t\tWELCOME TO FELIPE'S TAGUERIA")
    print(f"{'='*50}")


def main():
    """
    Main menu loop.
    Dictionary records orders.
    """
    invoice = {}
    start_banner()
    while True:
        menu = import_json("taqueria.json")
        view_menu(menu)
        generate_invoice(invoice)
        item, cost = get_order(
            menu,
            "Menu Number or 0 to Exit: ")
        invoice[item] = cost


if __name__ == "__main__":
    main()
