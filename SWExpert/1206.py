# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2,n-2):
        if lst[i] > max(lst[i - 2:i]) and lst[i] > max(lst[i + 1:i + 3]):
            cnt = cnt + lst[i] - max(lst[i-2:i]) if max(lst[i-2:i]) > max(lst[i+1:i+3]) else cnt + lst[i] - max(lst[i+1:i+3])
    print(f"#{case+1} {cnt}")