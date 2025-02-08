def add_finished(func):
    def wrapper(*args):
        result = func(*args)
        print('finished')
        return result
    return wrapper


@add_finished
def print_text():
    print('print me')


print_text()


@add_finished
def calc(x, y):
    print((x + y) * 2)


calc(4, 5)


@add_finished
def print_start():
    print('start')


print_start()
