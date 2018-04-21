def plural_form(num, form1, form2, form5):
    if 10 < num % 100 < 20:
        return form5
    elif num % 10 == 1:
        return form1
    elif 2 <= num % 10 <= 4:
        return form2
    return form5


b = str(input('Я угадаю твой возраст. Хочешь? '))
if b.lower().capitalize() in ['Да', 'Давай', 'Конечно', 'Хочу']:
    print('Умножь свой возраст на 5')
    print('Прибавь 8')
    print('Умножь на 2')
    print('Вычти 6')
    print('Умножь на 10')
    a = int(input('Напиши получившееся число '))
    a -= 100
    a /= 100

    print('Тебе ', int(a), plural_form(a, 'год', 'года', 'лет'))
elif b == 'Нет' or 'Не надо' or 'Не хочу':
    print('Не очень-то и хотелось!')
else:
    print('Я тебя не понимать')
