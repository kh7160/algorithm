import sys
sys.setrecursionlimit(10000)
tmp = [0] * 1000000

def solution(n):
    return Fin(n) % 1234567


def Fin(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    if tmp[n-1] != 0:
        return tmp[n-1]
    else:
        tmp[n-1] = Fin(n - 2) + Fin(n - 1)
        return tmp[n-1]

print(solution(100000))