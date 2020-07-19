# import sys, time
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    lst = iter(list(map(int, input().split(' '))))
    max_lst = max(lst)
    re_idx = 0
    rslt = 0
    for i in lst:
        if lst == max_lst:
            rslt += sum([max_lst - _ for _ in lst[re_idx:]])

            if i != len(lst)-1:
                re_idx = i+1
                max_lst = max(lst[re_idx:])

    while True:
        if lst[re_idx] == max_lst:
            rslt += sum([max_lst - _ for _ in lst[re_idx:i]])
            max_lst = max(lst[re_idx+1:])
        re_idx += 1
    print(f"#{case+1} {rslt}")