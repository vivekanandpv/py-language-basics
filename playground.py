def division(numerator, denominator):
    return (numerator / denominator)


# General exception handler
try:
    division(3, 0)
except:
    print('Exception raised')

# Specific exception handler
try:
    division(3, 0)
except ZeroDivisionError:
    print('ZeroDivisionError')

# Multiple except blocks in sequence
try:
    division(3, 0)
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('General error')

# Using else in case the exception is not raised
try:
    division(3, 0)
except:
    print('Exception raised')
else:
    print('No error')

# Combined except handlers and catching error object:
try:
    division(2, 0)
except (ZeroDivisionError, SyntaxError) as e:
    print(f'Error caught: {e}')


# Finally
try:
    division(2, 0)
except:
    print(f'Error caught: {e}')
finally:
    print('Will run anyway')

# Raising error
try:
    raise TypeError('Voluntary raising of error')
except TypeError as e:
    print(f'Error caught: {e}')
finally:
    print('Finally')
