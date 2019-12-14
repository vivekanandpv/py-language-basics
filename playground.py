# when decorators are applied, the metadata of
# the wrapper is used instead of the
# function/method
# To fix this, use functools.wraps(f) decorator
# for wrapper function

from functools import wraps


def upper_case(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return result.upper()

    return wrapper


def get_name(name):
    '''This is the get_name(name) function'''
    return name


print(f'get_name: {get_name("sherlock holmes")}')
print(f'get_name.__doc__: {get_name.__doc__}')
