import itertools
n, m = map(int, input().split())
card = list(map(int, input().split()))
# print(card)
pb_lst = list(itertools.permutations(card, 3))
fnl = 0
for _ in pb_lst:
    # print(sum(_))
    sum_num = sum(_)
    if sum_num > m:
        continue
    elif sum_num == m:
        fnl = sum_num
        break
    elif sum_num < m and fnl < sum_num:
        fnl = sum_num

print(fnl)