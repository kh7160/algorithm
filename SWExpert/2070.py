# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    result = '<' if a < b else\
             '>' if a > b else\
             '='
    print(f"#{i+1} {result}")