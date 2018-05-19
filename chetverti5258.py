g = [[-3, 4], [1, 2], [1, 1], [0, 4], [-2, -3], [-6, 8], [-12, 1]]

#     M  R  x  y
# p = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
p = []
for i in range(5):
    p.append([0]*4)
# p = [[0, 0, 0, 0]]*5 - никогда так не делайте :))))))
# потому что создаются клоны списка, которые заполняются одновременно
for i in range(len(g)):
    x, y = g[i][0], g[i][1]
    R = min(abs(x), abs(y))
    if x > 0 and y > 0:
        K = 1
    if x < 0 and y > 0:
        K = 2
    if x < 0 and y < 0:
        K = 3
    if x > 0 and y < 0:
        K = 4
    if x != 0 and y != 0:
        p[K][0] += 1
        if p[K][1] == 0 or p[K][1] > R:
            p[K][1] = R
            p[K][2] = x
            p[K][3] = y

maxM = 0
minR = p[1][1]
for i in range(1, len(p)):
    if p[i][0] > maxM:
        maxM = p[i][0]
        K = i
    elif p[i][0] == maxM:
        if p[i][1] < minR:
            minR = p[i][1]
            K = i

print('K = ', K)
print('M = ', p[K][0])
print('A = (', p[K][2], ',', p[K][3], ')')
print('R = ', p[K][1])