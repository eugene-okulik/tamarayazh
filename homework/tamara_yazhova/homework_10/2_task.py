def counter_func(func):
    def wrapper(*args, count=1):
        for i in range(count):
            func(*args)
    return wrapper


@counter_func
def example(text):
    print(text)


example('print me', count=5)


@counter_func
def example2():
    print('repeat this')


example2(count=3)
