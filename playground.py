# Syntax: for x in iterable
# break and continue work the same way
for i in range(1, 100, 3):
    if i % 2 == 0:
        continue
    print(f'Custom range {i}')

# list, tuple, dictionary, set - are iterables
for city in ('Bengaluru', 'Mysuru', 'Mumbai'):
    print(f'City: {city}')

# Using else with for
for item in range(10):
    print(f'Normal range: {item}')
else:
    print('Normal range iterator completed')
