# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for num in range(t):
    n, k = map(int, input().split(' '))
    arr = [input().split(' ') for _ in range(n)]
    cnt = 0
    # print(_ + 1)
    for i in range(n):
        for j in range(n):
            row_cnt = 0
            col_cnt = 0
            if arr[i][j] == '1' and True if (j == 0 or arr[i][j-1] == '0') else False:
                for _ in range(j, n):
                    if arr[i][_] == '1':
                        row_cnt += 1
                    else:
                        break
            if arr[i][j] == '1' and True if (i == 0 or arr[i-1][j] == '0') else False:
                for _ in range(i, n):
                    if arr[_][j] == '1':
                        col_cnt += 1
                    else:
                        break
            if row_cnt == k or col_cnt == k:
                if row_cnt == k and col_cnt == k:
                    cnt += 2
                else:
                    cnt += 1
                # print(i,j)
            # print(row_cnt, col_cnt)
    print(f"#{num+1} {cnt}")