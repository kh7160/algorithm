# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    while n != 0:
        max_idx, min_idx = lst.index(max(lst)), lst.index(min(lst))
        if lst[max_idx] - lst[min_idx] == 0 or lst[max_idx] - lst[min_idx] == 1:
            break
        lst[max_idx] -= 1
        lst[min_idx] += 1
        n -= 1
    print("#{} {}".format(case+1, lst[lst.index(max(lst))] - lst[lst.index(min(lst))]))