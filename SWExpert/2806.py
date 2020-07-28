# import sys
# sys.stdin = open("input.txt", "r")
col_chk = []
row_chk = []
cnt = 0

def brute_force(table, col, row):
    if col_chk[col] == False or row_chk[row] == False:
        if cnt == n:
            cnt += 1
        return
    for i in range(col, n):
        for j in range(row, n):

    pass

t = int(input())
for case in range(t):
    n = int(input())
    col_chk = [False] * n
    row_chk = [False] * n
    cnt = 0
    table = [[0 for _ in range(n)] for _ in range(n)]