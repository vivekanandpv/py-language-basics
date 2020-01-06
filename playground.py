# Exercise:

# create a function get_amount, which returns a decimal number.

# create a decorator which extends get_amount by:
# 1.	applying indian rupee symbol
# 2.	rounding off decimal places to 2


def indian_rupee(f):
    # define a wrapper function
    def wrapper(*args, **kwargs):
        amount = f(*args, **kwargs)
        amount = round(amount, 2)
        return f'₹ {amount}'

    # return the wrapper function
    return wrapper


@indian_rupee
def get_amount(amount):
    return amount


print(f'result: {get_amount(123.457788)}')
