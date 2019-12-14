# higher order functions:
#   a. functions that take other functions as parameters
#   b. functions that return functions

# higher-order function: callback function example


def foo(val, callback):
    callback(val)


foo(100, lambda v: print(f'callback: {v}'))

# higher-order functions: closure example


def coffee_maker(counter):
    def dispence_coffee():
        # global for module level name binding
        nonlocal counter
        counter += 1
        print(f'dispensing... {counter}')

    return dispence_coffee


dispenser = coffee_maker(0)

dispenser()
dispenser()
dispenser()
dispenser()
