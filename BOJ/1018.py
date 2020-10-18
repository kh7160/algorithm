n, m = map(int, input().split())
tot = [list(input()) for _ in range(n)]
result = 999999999
for out_i in range(n-7):
    for out_j in range(m-7):
        w_color = [('W', 'B'), ('B', 'W')]
        w_cnt = 0

        for i in range(out_i, out_i + 8):
            for j in range(out_j, out_j + 8):
                if tot[i][j] != w_color[(i-out_i)%2][(j-out_j)%2]:
                    w_cnt += 1

        b_color = [('B', 'W'), ('W', 'B')]
        b_cnt = 0

        for i in range(out_i, out_i + 8):
            for j in range(out_j, out_j + 8):
                if tot[i][j] != b_color[(i-out_i)%2][(j-out_j)%2]:
                    b_cnt += 1

        result = min(result, w_cnt)
        result = min(result, b_cnt)
print(result)
