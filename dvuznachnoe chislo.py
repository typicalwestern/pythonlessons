input('Загадай двузначное число')
a = int(input('Раздели на 3 и напиши остаток '))
b = int(input('Раздели на 5 и напиши остаток '))
c = int(input('Раздели на 7 и напиши остаток '))
a = a * 70
b = b * 21
c = c * 15
summ = (a + b + c) % 105
print('Твоё число', summ)
