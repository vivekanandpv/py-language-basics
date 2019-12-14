class Logger:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.enabled:
                print(f'Logging...')
            return f(*args, **kwargs)

        return wrapper


logger = Logger()


@logger
def get_name(name):
    print(f'get_name: {name}')


get_name('Mahesh')
get_name('Mukul')

logger.enabled = False

get_name('Arvind')
