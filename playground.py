x = 100

x += 1  # x++ is syntax error,
# Other operators: *=, /=, -=


# x+=1 is not allowed in print()
print(x)

y = 10 ** 2  # exponentiation (10^2)
print(y)
# exponentiation works with floats as operands as well
print(3.345**0.214)

a = 20 // 3  # floor division 6.66666... => 6
# result is of int type
print(f'value: {a}, type {type(a)}')

# floor division works with floats as operands as well
b = 3.345 // 0.214
# If one operand is float result is float
print(f'value: {b}, type {type(b)}')

# also available: //= and **=
