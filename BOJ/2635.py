# import sys, copy
# sys.stdin = open("input.txt", "r")
import copy

n = int(input())
rslt_lst = []
for i in range(1, n+1):
    tmp_lst = []
    first = n
    second = i
    tmp_lst.append(first)
    tmp_lst.append(second)
    while True:
        diff = first - second
        if diff < 0:
            break

        tmp_lst.append(diff)
        first, second = second, diff

    if len(tmp_lst) > len(rslt_lst):
        rslt_lst = copy.deepcopy(tmp_lst)

print(len(rslt_lst))
print(*rslt_lst)