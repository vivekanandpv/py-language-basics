class Car:
    # __init__ is not a constructor
    # constructor is provided by the runtime

    # all instance methods should take self
    # as the first argument

    def __init__(self, name='Default'):
        self._name = name

    def get_name(self):
        return self._name


car_one = Car()
car_two = Car('MG Hector')

print(f'car_one.get_name(): {car_one.get_name()}')
print(f'car_two.get_name("MG Hector"): {car_two.get_name()}')
