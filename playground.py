# Decorators are higher order functions
# Decorator takes an existing function
# and returns another function
# This way, the existing function can be extended


def upper_case(f):
    print(f'upper_case called {f}')

    def wrapper(*args, **kwargs):
        print(f'upper_case wrapper called args: {args} kwargs: {kwargs}')
        result = f(*args, **kwargs)
        print(f'wrapper got: {result}, and returning')
        return result.upper()

    print('upper_case returning')
    return wrapper


@upper_case
def get_city(x, y):
    print('get_city called')
    return 'bengaluru'


print(f'final result: {get_city("value of x", y=1200)}')
