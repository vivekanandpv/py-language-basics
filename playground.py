# decorators are called in bottom up manner


def lower_case(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return result.lower()

    return wrapper


def title_case(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return result.title()

    return wrapper


@title_case  # second applied
@lower_case  # first applied
def get_name(name):
    return name


print(f'get_name: {get_name("aNNa KAREnina")}')
