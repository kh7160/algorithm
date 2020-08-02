# import sys
# sys.stdin = open("input.txt", "r")

ways = [(0,1),(1,0)]
n = int(input())
table = [list(input()) for _ in range(n)]
# print(table)
total_max = 0

def table_sum():
    table_max = 0
    for i in range(n):
        for j in range(i,n-1):
            cnt = 1
            for k in range(n-1):
                if table[j][k] == table[j][k+1]:
                    # print(i, k, table[j][k], table[j][k+1])
                    cnt += 1
                else:
                    # print('break')
                    break
            table_max = cnt if cnt > table_max else table_max

        for j in range(i, n - 1):
            cnt = 1
            for k in range(n-1):
                if table[k][j] == table[k + 1][j]:
                    # print(k, k+1, table[k][j], table[k + 1][j], cnt)
                    cnt += 1
                else:
                    # print('break')
                    break
            table_max = cnt if cnt > table_max else table_max
    return table_max

for i in range(n-1):
    for j in range(n-1):
        for _next in ways:
            # print(_next[0], _next[1])
            table[i][j], table[i+_next[0]][j+_next[1]] = table[i+_next[0]][j+_next[1]], table[i][j]
            temp = table_sum()
            total_max = temp if temp > total_max else total_max
            table[i][j], table[i+_next[0]][j+_next[1]] = table[i+_next[0]][j+_next[1]], table[i][j]

print(total_max)
