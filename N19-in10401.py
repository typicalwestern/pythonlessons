A = [0, 2, 3, 4, 4, 10, 4, 5, 6, 12, 9]
n = 10
s = 0
print(A)
for i in range(2, n + 1):
    if A[i - 1] < A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]
        A[i] += 1
        s += 1

print(A)
