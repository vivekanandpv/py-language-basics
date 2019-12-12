x = True
y = False

# Or operator
if x or y:
    print(f'Logical OR operator: {x} or {y}')

# And operator
if x and y:
    print('I don\'t see this')
else:
    print(f'Else block for {x} and {y}')

# Not operator
if not y:
    print('Inverting y')

# Complex expression
if (x or y) and (not y):
    print('Learning complex boolean expressions')
