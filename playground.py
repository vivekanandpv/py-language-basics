class Vehicle:
    # everything is inherited
    # inheritance is used to reuse implementation
    def __init__(self, name='Default'):
        self._name = name


class Car(Vehicle):

    def get_name(self):
        return self._name


car_one = Car()
car_two = Car('MG Hector')

print(f'car_one.get_name(): {car_one.get_name()}')
print(f'car_two.get_name("MG Hector"): {car_two.get_name()}')
