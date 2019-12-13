# A set is mathematical in its notion
# Order is irrelevant
# cannot change the existing elements
# but can add and remove
# set operations are allowed
letters = {'A', 'B', 'C'}

# A set is an iterable collection
for el in letters:
    print(f'element: {el}')

# existence
print('Z' in letters)

# add
letters.add('D')
# existence matters, order is irrelevant
print(f'letters after add: {letters}')

# remove
letters.remove('C')
print(f'letters after remove: {letters}')
# discard can also be used
# pop(), though works, is not recommended as the order cannot be presumed

# adding duplicate is not an error, but has no effect
letters.add('A')
print(f'letters after adding duplicate: {letters}')
