#   Strings can be written in single or double quotes.
#   There is no character type.
name = 'Wilson Jacob'
city = "Wisconsin"

#   String concatenation
print('Name: ' + name + '; city: ' + city)

#   Formatted strings
print(F'Name: {name}; city: {city}')  # F is also allowed, but f is conventionally used

#   Multiline strings
print('''This is a multiline
note for all the students
of computer science.''')  # You can use double quotes instead

#   Unicode is directly supported in Python 3.x
print('''नमस्ते''')

#   You can also use unicode code units
#   This is Python 2.x style
print(u'\u265E')  # Chess black night

#   In Python 3.x, we can directly embed the character we want
print('♞')

#   Python 2.x formatted strings (uses indexes)
print('Name: {0}; city: {1}'.format(name, city))

#   Other variants

#   without indexes
print('Name: {}; city: {}'.format(name, city))

#   named placeholders
print('Name: {user_name}; city: {user_city}'.format(user_name=name, user_city=city))

#   Providing other formatting
pi = 3.141592635
print('π = {math_pi:.4f}'.format(math_pi=pi))

#   Some useful formatting types:
#   https://docs.python.org/3.4/library/string.html#format-specification-mini-language
