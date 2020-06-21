# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
temp_sum = 0
for i in range(len(str(n))):
    n, temp = n // 10, n % 10
    temp_sum += temp
print(f"{temp_sum}")