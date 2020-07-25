# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    table = [list(map(int, input())) for _ in range(n)]
    # print(table)
    idx = 1
    rslt = 0
    for j in range(n):
        start = n//2 - j if j <= n//2 else j - n // 2
        end = n//2 + j if j <= n//2 else n - 1 + (n//2 - j)
        rslt += sum(table[j][start:end+1])
        # print(start, end, table[j][start:end+1])
    print(f"#{case+1} {rslt}")