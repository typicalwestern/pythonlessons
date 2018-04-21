from math import sqrt, floor

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
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
