# import sys, math
# sys.stdin = open("input.txt", "r")
import math
t = int(input())
for case in range(t):
    n = int(input())
    lst = input().split()
    odd_lst = lst[:math.ceil(len(lst)/2)]
    even_lst = lst[math.ceil(len(lst)/2):]
    rst_lst = []
    # print(odd_lst, even_lst)
    for _ in range(len(even_lst)):
        rst_lst.append(odd_lst[_])
        rst_lst.append(even_lst[_])

    if len(lst) % 2 == 1:
        rst_lst.append(odd_lst[len(odd_lst)-1])

    print("#" + str(case+1), end=' ')
    print(*rst_lst)