def minlength(length):
    def validator(f):

        def wrapper(*args):
            # print(f'args: {args}')
            if len(args[0]) < length:
                raise ValueError(f'Minimum length is {length}')
            return f(*args)

        return wrapper

    return validator


@minlength(5)
def get_input(name):
    print(f'get_input: {name}')


get_input('Vivek')
