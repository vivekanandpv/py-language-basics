# lambda is a convenient way to pass
# an anonymous callback function


def foo(val, bar):
    bar(val)


foo(100, lambda v: print(f'lambda executes: {v}'))


# named function for using as a call back
def named_bar(number):
    print(f'named function executes: {number}')


foo(100, named_bar)
