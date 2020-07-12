# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n, m = map(int, input().split(' '))
    max_sum = 0
    a_arr = list(map(int, input().split(' ')))
    b_arr = list(map(int, input().split(' ')))
    if len(a_arr) > len(b_arr):
        max_arr, min_arr = a_arr, b_arr
    else:
        max_arr, min_arr = b_arr, a_arr

    for i in range(len(max_arr) - len(min_arr) + 1):
        tmp_arr = max_arr[i:i+len(min_arr)]
        tmp_sum=0
        for j in range(len(tmp_arr)):
            tmp_sum += tmp_arr[j] * min_arr[j]
        max_sum = tmp_sum if tmp_sum > max_sum else max_sum
    print(f"#{case+1} {max_sum}")