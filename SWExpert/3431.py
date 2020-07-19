# import sys, time
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    l,u,x = map(int, input().split(' '))
    rslt = l - x if l > x else\
           -1    if x > u else\
           0
    print(f"#{case+1} {rslt}")