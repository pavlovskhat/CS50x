"""
CS50 task4.4
Converts date inputs to ISO 8601.
"""
date_data = {
    ["jan", "january"]: 31,
    ["feb", "february"]: 28,
    ["mar", "march"]: 31,
    ["apr", "april"]: 30,
    ["may",]: 31,
    ["jun", "june"]: 30,
    ["jul", "july"]: 31,
    ["aug", "august"]: 31,
    ["sep", "september"]: 30,
    ["oct", "october"]: 31,
    ["nov", "november"]: 30,
    ["dec", "december"]: 31,
}


def string_replace(string: str, chars: list) -> str:
    for char in chars:
        string = string.replace(char, " ")
    return string


def get_chars(string: str) -> list:
    chars = []
    for char in string:
        if not char.isalpha():
            chars.append(char)
    return chars


def main():
    input_date = input("Enter date: ")
    cleaned_date = string_replace(
        input_date,
        get_chars(input_date)
    )
    print(cleaned_date)
    for months in date_data.keys():
        for part in cleaned_date.split():
            if part in months:



if __name__ == "__main__":
    main()
