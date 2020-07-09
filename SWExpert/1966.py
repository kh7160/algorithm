# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    tmp = map(int, input().split(' '))
    tmp = sorted(tmp)
    print(f"#{case+1}", end=' ')
    print(*tmp)