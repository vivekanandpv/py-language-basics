# tuples are immutable lists for practical considerations
# duplicates may exist
vowels = ('a', 'e', 'i', 'o', 'u')

# to create a tuple of only one element,
# add trailing comma x = ('el',)

# please note, tuples cannot add, remove, mutate
# but a tuple variable can get a new reference
# akin to string assignments

# del deletes the whole tuple
# a new tuple can be created by joining two tuples
numbers = (0, 1, 2, 3)

new_tuple = numbers + vowels
print(f'new_tuple: {new_tuple}')


# existence check
if 'a' in vowels:
    print('a is found in the tuple')

# len() operator
print(f'length of the tuple: {len(vowels)}')
