def decorator_of_calc(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@decorator_of_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input("Введите число: "))
second = int(input("Введите второе число: "))


print(calc(first, second))
