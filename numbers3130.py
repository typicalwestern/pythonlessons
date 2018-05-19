while True:
    N = int(input('input n'))
    if 0 < N <= 100:
        break
    print('input 0 < n <= 100!')

print(N)

while True:
    tmp = input('blabla')
    print(tmp)
    # tmp = tmp.split(' ')
    print(tmp[:N])
    if len(tmp) == N:
        break
    print('Ты облажался с количеством элементов')
