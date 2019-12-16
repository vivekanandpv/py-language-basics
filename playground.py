# Decorators are higher order functions
# Decorator takes an existing function
# and returns another function
# This way, the existing function can be extended


def upper_case(f):
    print('upper_case called')

    def wrapper(*args, **kwargs):
        print('upper_case wrapper called')
        result = f(*args, **kwargs)
        print(f'wrapper got: {result}, and returning')
        return result.upper()

    print('upper_case returning')
    return wrapper


@upper_case
def get_city():
    print('get_city called')
    return 'bengaluru'


print(f'final result: {get_city()}')
