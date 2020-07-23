# import sys, time
# sys.stdin = open("input.txt", "r")

n = int(input())
for case in range(n):
    t = int(input())
    block = list(map(int, input().split()))
    down_max = 0
    up_max = 0
    for i in range(t-1):
        if block[i] < block[i+1]:
            up_max = block[i+1] - block[i] if block[i+1] - block[i] > up_max else up_max
        elif block[i] > block[i+1]:
            down_max = block[i] - block[i+1] if block[i] - block[i+1] > down_max else down_max

    print(f"#{case+1} {up_max} {down_max}")