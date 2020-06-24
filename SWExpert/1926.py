# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for _ in range(1,n+1):
    cnt = str(_).count('3') + str(_).count('6') + str(_).count('9')
    if cnt != 0:
        print(cnt * '-', end=' ')
    else:
        print(_, end=' ')