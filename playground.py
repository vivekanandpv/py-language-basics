# Exercise:

# Create a function that takes arbitrary arguments of numbers

# This function should return the sum of squares of only odd numbers passed to it


# Solution:

# We take arbitrary arguments as *numbers
def do_work(*numbers):
    # numbers (NOT *numbers) is a tuple inside
    sum = 0

    for n in numbers:
        if n % 2 != 0:
            sum += n**2

    return sum


print(do_work(1, 2, 3, 4, 5, 6, 7))
print(do_work())
print(do_work(2, 4, 6, 8, 1))
