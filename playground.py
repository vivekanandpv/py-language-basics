from math import factorial
print({len(str(factorial(n))) for n in range(20) if (n % 2 == 0)})
