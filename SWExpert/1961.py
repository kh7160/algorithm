# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    tmp = [[_ for _ in map(int, input().split(' '))] for _ in range(n)]
    tmp_90 = [[tmp[j][i] for j in range(n - 1, -1, -1)] for i in range(n)]
    tmp_180 = [[tmp[i][j] for j in range(n - 1, -1, -1)] for i in range(n - 1, -1, -1)]
    tmp_270 = [[tmp[j][i] for j in range(n)] for i in range(n - 1, -1, -1)]
    print("#{}".format(case+1))
    for _ in range(n):
        print(*tmp_90[_], end=' ', sep='')
        print(*tmp_180[_], end=' ', sep='')
        print(*tmp_270[_], end='\n', sep='')