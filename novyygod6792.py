N = int(input('input amount of matinees'))
snegurkaNotepadCounter = [0] * 100
for i in range(N):
    tmp = input('input kids and candies separated with space')
    d, k = tmp.split(' ')
    d = int(d)
    k = int(k)
    if k % d > 0:
        snegurkaNotepadCounter[k % d] += 1

max_records = 0
max_records_num = 0
for i in range(1, 100):
    if snegurkaNotepadCounter[i] > max_records:
        max_records = snegurkaNotepadCounter[i]
        max_records_num = i
    elif snegurkaNotepadCounter[i] == max_records and i > max_records_num:
        max_records_num = i

print(max_records_num)
