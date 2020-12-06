#   documentation: https://docs.python.org/3.4/library/stdtypes.html#string-methods

sample = 'this is a sample text for you'

#   Capitalizes the first character of the string
print(sample.capitalize())

#   Use casefold for case-agnostic matching
print('First'.casefold() == 'fiRst'.casefold())

#   Use center to get the string padded with character of choice (space is default)
#   second parameter should be exactly 1 character
#   This has left-bias (play with even and odd width here)
print('Topic'.center(12, '~'))

#   count returns the number of non-overlapping occurances of a substring
print('The name that can be named is not the eternal name'.count('name'))

#   endswith and startswith
print('CustomerController'.endswith('Controller'))
print('CustomerController'.startswith('Customer'))

#   find the substring
#   -1 if not found
#   The default direction is from left
#   rfind and rindex work from right side
print('He went on to become a good engineer'.find('good'))

#   index is like find, but raises ValueError if substring is not found
print('He went on to become a good engineer'.index('good'))

#   to check if the string is alpha-numeric (no special characters)
print('ABCD1234'.isalnum())

#   to check if the string is all characters (no special characters including space!)
print('I drive a car'.isalpha())  # False because of spaces!
print('UnitedStatesOfAmerica'.isalpha())

#   to check if the string contains numbers
#   these functions are almost equal for general use
#   but the when unicode-specific numerics are used they behave differently
print('124'.isnumeric())
print('124'.isdigit())
print('124'.isdecimal())

#   ½ is one character
print('½'.isnumeric())  # True
print('½'.isdigit())  # False
print('½'.isdecimal())  # False

#   ³ is superscript
print('³'.isnumeric())  # True
print('³'.isdigit())  # True
print('³'.isdecimal())  # False

#   to check the case
print('all lowercase letters'.islower())
print('ALL UPPERCASE LETTERS'.isupper())
print('This Follows Title Case Convention'.istitle())

#   case conversion
print('To LoWeRcAsE'.lower())
print('tO uPpErCase'.upper())
print('tO tiTLE'.title())

#   splitting
print('A B C D E F'.split())  # splits at space
print('A;B;C;D;E;F'.split(';'))  # splits at delimiter ;
print('A;B;C;D;E;F'.split(';', maxsplit=2))  # splits at delimiter ; only two splits

print('''This is a 
multiline
string'''.splitlines())  # splits at newline

#   stripping the whitespace at both ends
print('   Did I strip the whitespace?    '.strip())

#   zero-padding to the left
print('3.141592635'.zfill(12))

print('Hi there!'.zfill(15))    # doesn't make sense, but still works


