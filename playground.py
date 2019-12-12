# Integers
print(type(100))  # int

# Floating-point Numbers
# float is actually a double-precision floating point number (64-bit)
print(type(3.14159265359))

# Complex numbers
print(type(2 - 3j))

# Strings (type is called str)
print(type("Hello there"))

# Booleans (type is called bool)
print(type(True))  # First letter is capital!

# Function
print(type(lambda x: None))

# Built-in functions or methods (globally available)
print(type(abs))    # builtin_function_or_method

# ----------------
# Collection types

# List (array)
print(type([1, True, 'Hello']))

# Tuple (read-only array)
print(type((1, 3.1454, 'Oh!', False)))

# Dictionary (map)
print(type({'country': 'India', 'code': 'IN'}))  # dict

# Set (for unique elements)
print(type({100, 2.789, 'Bengaluru'}))
