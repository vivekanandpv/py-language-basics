# default parameters
def foo(year=2019):
    year += 1
    return year


print(foo())

# keyword arguments


def bar(year, month, day):
    print(f'year: {year}, month: {month}, day: {day}')


# non keyword argument should not come after keyword argument
# bar(month=8, 2019, 1) is SyntaxError
bar(day=10, year=2019, month=7)

# arbitrary arguments
# arguments become a tuple
# * should come at the end


def baz(first, *args):
    print(f'first: {first}')
    for arg in args:
        print(f'arg: {arg}')


baz(2019, 1, 2, 3, 4, 5, 6, 7, 8, 9)
