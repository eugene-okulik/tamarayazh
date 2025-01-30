def fibonachi(limit=100001):
    a, b = 0, 1
    counter = 1
    while counter < limit:
        yield a
        a, b = b, a + b
        counter += 1

count = 1
for x in fibonachi(100001):
    if count == 5:
        print(f'5-ое число Фибоначи: {x}')
    elif count == 200:
        print(f'200-ое число Фибоначи: {x}')
    elif count == 1000:
        print(f'1000-ое число Фибоначи: {x}')
    elif count == 10000:
        print(f'10000-ое число Фибоначи: {x}')
        break
    count += 1
