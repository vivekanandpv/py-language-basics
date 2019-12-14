# Syntax [expr(item) for item in iterable]

from math import factorial
words = 'I am here to learn list comprehensions'.split()

print([len(word) for word in words])

factorials = [factorial(n) for n in range(20)]

print([len(str(item)) for item in factorials])

# or
print([len(str(factorial(n))) for n in range(20)])
