def range_clone(start=0, end=10):

    index = start

    while index <= end:
        yield index
        index += 1


for i in range_clone(end=20):
    print(f'range_clone: {i}')


def fibonacci(start=1, end=100):
    a = start
    b = start

    while b < end:
        a, b = b, a + b
        yield a


for i in fibonacci(end=20):
    print(f'Fibonacci: {i}')


def get_distinct(iterable):
    items = set()

    for item in iterable:
        if item in items:
            continue
        else:
            yield item
            items.add(item)


for i in get_distinct([1, 2, 3, 4, 5, 4, 3, 2, 1, 6, 7, 8]):
    print(f'distinct: {i}')
