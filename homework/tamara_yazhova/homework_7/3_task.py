def add_numbers(string):
    return int(string[string.index(':') + 1:]) + 10


def find_numbers():
    text = [
        "результат операции: 42",
        "результат операции: 54",
        "результат работы программы: 209",
        "результат: 2"
    ]

    for string in text:
        print(add_numbers(string))

find_numbers()
