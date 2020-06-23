# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    a,b = map(int, input().split(' '))
    div, mod = a // b, a % b
    print(f"#{i+1} {div} {mod}")