# list is ordered collection that supports change

vowels = ['a', 'e', 'i', 'o', 'u']

# Accessing by index
print(f'[2]: {vowels[2]}')  # i

# Syntax [-x] considers from the end.
# -1 is end -0 is beginning!
# if x exceeds the length (both [x] and [-x]),
# IndexError is thrown

# Selection
print(f'[0:3] {vowels[0:3]}')  # a, e, i

# Syntax: [x:y]
# where x is the starting index (included)
# y is the ending index (not included)
# mathematically: [x, y)
# if x is absent, 0 is default
# if y is absent, end is presumed
# if x or y or both are > length, there is error
# but the result is empty
