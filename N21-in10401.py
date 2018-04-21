def f(x):
    return 2 * (x - 1) * (x - 3) + 7


a = -9
b = 9
M = a
R = f(a)
for t in range(a, b + 1):
    if f(t) > R:
        M = t
        R = f(t)
print(M + R)
