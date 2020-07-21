# import sys, time
# sys.stdin = open("input.txt", "r")

n = int(input())
skip_lst = ['a', 'e', 'i', 'o', 'u']
for case in range(n):
    line = input()
    result = ''.join([_ for _ in line if _ not in skip_lst])
    print(f"#{case+1} {result}")