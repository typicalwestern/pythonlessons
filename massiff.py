from random import randint

N = 30

i = None

j = None

k = None

a = [int(randint(0, 100)) for i in range(N)]

print(a)

k, j = 0, 1
for i in range(1, N):
    if a[i - 1] < a[i]:
        j += 1
        if j > k: k = j
    else: j = 1
print(k)
