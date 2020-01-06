# Exercise:

# create a function get_amount, which returns a decimal number.

# create a decorator which extends get_amount by:
# 1.	applying indian rupee symbol
# 2.	rounding off decimal places to 2


def currency(country):
    # define a wrapper function
    def wrapper(f):
        def inner_wrapper(*args, **kwargs):
            amount = f(*args, **kwargs)
            amount = round(amount, 2)

            if (country.lower() == 'india'):
                return f'₹ {amount}'
            elif (country.lower() == 'usa'):
                return f'$ {amount}'
            elif (country.lower() == 'europe'):
                return f'€ {amount}'
            else:
                return f'Unknown {amount}'

        return inner_wrapper

    # return the wrapper function
    return wrapper


@currency('indIA')
def get_amount(amount):
    return amount


print(f'result: {get_amount(123.457788)}')
