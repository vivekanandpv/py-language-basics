# A set supports mathematical notions such as:
# union, intersection, difference

# subset and superset flags

even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
natural_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(
    f'even_numbers is the subset of natural_numbers: {even_numbers.issubset(natural_numbers)}')

print(
    f'natural_numbers is the superset of even_numbers: {natural_numbers.issuperset(even_numbers)}')

print(
    f'even_numbers and odd_numbers are disjoint: {even_numbers.isdisjoint(odd_numbers)}')

print(f'union of even and odd numbers: {odd_numbers.union(even_numbers)}')

print(
    f'intersection of even and natural numbers: {natural_numbers.intersection(even_numbers)}')

print(
    f'difference between natural and even numbers: {natural_numbers.difference(even_numbers)}')


# further reading: symmetric_difference
# intersection_update, difference_update,
# symmetric_difference_update
