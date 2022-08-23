print('1 = Addition\n' '2 = Subtraction\n' '3 = Multiplication\n' '4 = Division\n')
tipo = input('Select calc type: ')
x10 = input('First number = ')
x20 = input('Second number = ')
x1 = float(x10)
x2 = float(x20)

if tipo == '1':
    print('Equal to', x1 + x2)

if tipo == '2':
    print('Equal to', x1 - x2)

if tipo == '3':
    print('Equal to', x1 * x2)

if tipo == '4':
    print('Equal to', x1 / x2)
