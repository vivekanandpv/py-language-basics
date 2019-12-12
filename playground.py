vowels = []

# Add items
vowels.append('a')
vowels.append('e')
vowels.append('i')
vowels.append('o')
vowels.append('u')

print(f'vowels original: {vowels}')

# Mutation
vowels[0] = 'A'
print(f'vowels after mutation: {vowels}')

# Existence
if 'A' in vowels:
    print('A is found')
else:
    print('A is not found')

# Insert at an index
# right shifts
# if index is > length, no error thrown,
# but element is inserted at the end
vowels.insert(1, '?')
print(f'vowels after insert: {vowels}')

# remove by element
vowels.remove('?')
print(f'vowels after remove: {vowels}')

# pop
# end is presumed
# out of index is an error (IndexError)
vowels.pop(4)
print(f'vowels after pop: {vowels}')

# del
# del list deletes the list completely
# (object is deleted from memory)
del vowels[0]
print(f'vowels after del: {vowels}')

# clear - empties the list
vowels.clear()
print(f'vowels after clear: {vowels}')

# copy - create a shallow copy consider for value types
# in case the list contains objects,
# only references are copied
# x = y is just the reference copy
x = [1, 2, 3, 4]
y = x.copy()  # shallow copy, can consider y = x[:]
print(f'Are x and y same reference? {x is y}')
print(f'list x: {x}')
print(f'list y: {y}')

# joining two lists
a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(f'a + b = {c}')

# extending a list
a.extend(b)
print(f'a after extending: {a}')

# please check sort and reverse
