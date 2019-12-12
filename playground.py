# There is not C like for loop

# Basic syntax
index = 0

while index < 10:
    print(f'index: {index}')
    index += 1


# break
counter = 0

while counter < 20:
    if counter > 15:
        break
    else:
        print(f'counter: {counter}')

    counter += 1


# Using else with while loop
n = 10

while n < 10:
    print(f'n: {n}')
    n += 1
else:
    print('n >= 10')


# continue
p = 0

while p < 20:
    if (p % 2 != 0):
        print(f'p: {p}')
        p += 1
    else:
        p += 1
        continue
