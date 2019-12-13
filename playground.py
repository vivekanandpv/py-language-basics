# higher order functions:
#   a. functions that take other functions as parameters
#   b. functions that return functions

# higher-order function: callback function example


def foo(val, callback):
    callback(val)


foo(100, lambda v: print(f'callback: {v}'))

# higher-order functions: closure example


def coffee_maker(config):
    def dispence_coffee():
        config['counter'] += 1
        print(f'dispensing... {config.get("counter")}')

    return dispence_coffee


dispenser = coffee_maker({'counter': 0})

dispenser()
dispenser()
dispenser()
dispenser()
