class CallCounter:
    def __init__(self, f):
        print('__init__ called')
        self.f = f
        self.counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__ on CallCounter called')
        self.counter += 1
        return self.f(*args, **kwargs)

    def get_count(self):
        return self.counter


@CallCounter
def print_name(name):
    print(f'print_name: {name}')


print_name('Nitin')
print_name('Aditi')
print_name('Vinayak')
