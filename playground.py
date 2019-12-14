def division(numerator, denominator):
    return (numerator / denominator)


try:
    division(2, 0)
except (ZeroDivisionError, SyntaxError) as e:
    print(f'Error caught: {e}')
    raise
finally:
    print('Finally')
