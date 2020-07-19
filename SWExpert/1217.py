# import sys
# sys.stdin = open("input.txt", "r")

for _ in range(10):
    case = int(input())
    n,m = map(int, input().split(' '))
    F = lambda x,y=1: x if y == m else n*F(n,y+1)
    print(f"#{case} {F(n)}")