# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for i in range(n):
    temp_list = list(map(int, input().split(' ')))
    temp_max = max(temp_list)
    print(f"#{i+1} {temp_max}")