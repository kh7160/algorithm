# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    while lst[-1] != 0:
        for i in range(5):
            if i == 0 and lst[-1] != 0:
                lst.append(lst[0] - 1 if lst[0] -1 > 0 else 0)
                lst = lst[1:]
            elif i == 1 and lst[-1] != 0:
                lst.append(lst[0] - 2 if lst[0] -2 > 0 else 0)
                lst = lst[1:]
            elif i == 2 and lst[-1] != 0:
                lst.append(lst[0] - 3 if lst[0] -3 > 0 else 0)
                lst = lst[1:]
            elif i == 3 and lst[-1] != 0:
                lst.append(lst[0] - 4 if lst[0] -4 > 0 else 0)
                lst = lst[1:]
            elif i == 4 and lst[-1] != 0:
                lst.append(lst[0] - 5 if lst[0] -5 > 0 else 0)
                lst = lst[1:]
    print('#' + str(case+1), end=' ')
    print(*lst)