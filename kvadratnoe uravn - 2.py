from math import sqrt, floor

uravn = input('Введите уравнение:')
uravn = uravn.strip()
Negative = False
power = False
coeffs = ['', '', '']
current_coeff = 0
number_input = False
uravn = uravn.replace('-x', '-1x')
uravn = uravn.replace('+x', '+1x')
for symbol in uravn:
    if symbol == '-':
        Negative = True
    elif symbol == '^':
        power = True
    elif symbol.isdigit() or symbol == '.':
        if Negative:
            coeffs[current_coeff] += '-'
            Negative = False
        if not power:
            number_input = True
            coeffs[current_coeff] += symbol
        else:
            power = False
    elif symbol in 'x* ':
        pass

    if number_input and not symbol.isdigit():
        number_input = False
        current_coeff += 1

print(coeffs)
for i in range(len(coeffs)):
    coeffs[i] = float(coeffs[i])

# a = float(input('Введите a: '))
# b = float(input('Введите b: '))
# c = float(input('Введите c: '))
a, b, c = coeffs

print(a, 'x^2 + ', b, 'x + ', c, ' = 0', sep='')
if a == 0:
    if b == 0:
        if c == 0:
            print('x - любое число')
        else:
            print('Решения нет')
    else:
        # b != 0
        print('Ответ: ', -c / b)
else:
    D = b ** 2 - 4 * a * c
    print('D=', D)
    if D < 0:
        print('Действительных корней нет')
    elif D == 0:
        print('Ответ: ', -b / (2 * a), ' кратности 2')
    else:
        sq_D = sqrt(D)
        if floor(sq_D) == sq_D:
            print('Ответ: ', (-b - sqrt(D)) / (2 * a), ';', (-b + sqrt(D)) / (2 * a))
        else:
            print('Ответ: ', '(', -b, '- √', D, ') / (', 2 * a, ')', ';', '(', -b, '+ √', D, ') / (', 2 * a, ')',
                  sep='')
