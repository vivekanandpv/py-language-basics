generator_comprehension = ((n, n*n) for n in range(100) if (n % 3 == 0))

# <generator object <genexpr> at 0x000...>
print(generator_comprehension)

for i, j in generator_comprehension:
    # evaluation starts from this point
    print(f'generator comprehension: {i}: sq: {j}')


# load is significantly reduced
cube_generator = (n ** 3 for n in range(1000000))
print(f'sum of cubes: {sum(cube_generator)}')
