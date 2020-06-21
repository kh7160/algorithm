# import sys
# sys.stdin = open("input.txt", "r")
import math

n = int(input())
temp_list = list(map(int, input().split(' ')))
temp_list.sort()
temp_median = temp_list[math.floor(n/2)]
print(f"{temp_median}")