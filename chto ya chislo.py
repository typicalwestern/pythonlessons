interval_size = 2 ** 10

print('Загадайте число от 0 до %d' % (interval_size - 1))

st = 0
fin = interval_size

while st != (fin-1):
    mid = (fin - st) // 2 + st
    a = input('Это число меньше {} ?'.format(mid))
    if a.lower() in ['да', 'lf', 'zes', 'yes', 'ja', 'нуы', 'оф', 'oui', 'щгш']:
        fin = mid
    else:
        st = mid

print('Ваше число %d' % st)
