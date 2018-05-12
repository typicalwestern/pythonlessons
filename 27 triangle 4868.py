from random import randint

a = []

for i in range(20):
    x = randint(-10, 10)
    y = randint(-10, 10)
    if randint(1, 10) > 7:
        y = 0
    a.append((x, y))

print(a)

for i in range(-11, 12):
    out = ''
    for j in range(-11, 12):
        if (j, i) in a:
            out += '* '
        elif j == 0 and i == 0:
            out += '+ '
        elif j == 0:
            out += '| '
        elif i == 0:
            out += '--'
        else:
            out += '  '
    print(out)

# osvnovanie

minminus = 0
maxminus = 0
hminus = 0

minplus = 0
maxplus = 0
hplus = 0

for i in range(len(a)):
    p = a[i]
    # p[0] - x
    # p[1] - y
    x = p[0]
    y = p[1]
    if x == 0:
        continue
    if x < 0:
        if y == 0:
            # точка на оси Ох, слева от Оу
            if x < minminus:
                minminus = x
            if x > maxminus or maxminus == 0:
                maxminus = x
        else:
            if abs(y) > hminus:
                hminus = abs(y)
    else:
        if y == 0:
            # точка на оси Ох, слева от Оу
            if x > maxplus:
                maxplus = x
            if x < minplus or minplus == 0:
                minplus = x
        else:
            if abs(y) > hplus:
                hplus = abs(y)

print(minminus, maxminus, hminus)
sminus = (maxminus - minminus) * hminus / 2
print(minplus, maxplus, hplus)
splus = (maxplus - minplus) * hplus / 2

s = max(splus, sminus)
print(s)
