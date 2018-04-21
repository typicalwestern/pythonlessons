def func28(x):
    a = 0
    b = 0
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 6
        x = x // 6
    return a, b


for i in range(280, 1000000):
    a, b = func28(i)
    if a == 2 and b == 8:
        print(i)
        break
