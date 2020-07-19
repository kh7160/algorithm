# import sys, math
# sys.stdin = open("input.txt", "r")
import math

def circular_check(a):
    for i in range(math.ceil(len(a) / 2)):
        if a[i] == a[len(a) - (i + 1)]:
            pass
        else:
            return False
    return True

for _ in range(10):
    n = int(input())
    cnt = 0
    square = [[_ for _ in input()] for _ in range(8)]
    for i in range(8):
        for j in range(8 - n + 1):
            tmp = square[i][j:j+n]
            if circular_check(tmp) == True:
                cnt += 1

        for j in range(8):
            tmp = ''
            if i > 8 - n:
                break

            for k in range(i, n+i):
                tmp += square[k][j]
            # print(tmp)
            if circular_check(tmp) == True:
                cnt += 1

    print(f"#{_+1} {cnt}")