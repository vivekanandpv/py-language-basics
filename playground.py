# lambda is a convenient way to pass
# an anonymous callback function


def foo(val, bar):
    bar(val)


foo(100, lambda v: print(f'lambda executes: {v}'))
