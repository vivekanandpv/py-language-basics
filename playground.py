class Vehicle:
    year = 2019

    def __init__(self, name='Default'):
        self._name = name

    def get_area(self):
        return 'Ring Road'

    @staticmethod
    def get_city():
        return 'Bengaluru'

    @classmethod
    def get_country(cls):
        return 'India'


vehicle_one = Vehicle()
vehicle_one.year = 2020  # only in vehicle_one


vehicle_two = Vehicle()

print(f'vehicle_one.year: {vehicle_one.year}')  # 2020
print(f'vehicle_two.year: {vehicle_two.year}')  # 2019
print(f'Vehicle.year: {Vehicle.year}')  # 2019

print('---------------------------')

Vehicle.year = 2020  # changes everything

print(f'vehicle_one.year: {vehicle_one.year}')  # 2020
print(f'vehicle_two.year: {vehicle_two.year}')  # 2020
print(f'Vehicle.year: {Vehicle.year}')  # 2020

print('---------------------------')
print(f'Vehicle.get_city(): {Vehicle.get_city()}')
print(f'vehicle_one.get_city(): {vehicle_one.get_city()}')

# Static method can be called either on the class
# (such as C.f()) or on an instance
# (such as C().f()).
# The instance is ignored except for its class.
# https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod

print('---------------------------')
print(f'instance method: {vehicle_one.get_area}')

# Called on class; object is used only to get class
print(f'class method: {vehicle_one.get_country}')

# Like a plain function
print(f'static method: {vehicle_one.get_city}')
