n, m = map(int, input().split())
tot = [list(input()) for _ in range(n)]
result = 999999999
for out_i in range(n-7):
    for out_j in range(m-7):
        color = [('W', 'B'), ('B', 'W')] if tot[out_i][out_j] == 'W' else [('B', 'W'), ('W', 'B')]
        cnt = 0

        for i in range(out_i, out_i + 8):
            for j in range(out_j, out_j + 8):
                if tot[i][j] != color[(i-out_i)%2][(j-out_j)%2]:
                    cnt += 1
        result = min(cnt, result)
print(result)