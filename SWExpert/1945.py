# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
num = [2,3,5,7,11]
for case in range(t):
    n = int(input())
    idx = 0
    cnt = [0] * 5
    while n != 1:
        if n % num[idx] == 0:
            n /= num[idx]
            cnt[idx] += 1
        else:
            idx += 1
    print("#{} {} {} {} {} {}".format(case+1, *cnt))