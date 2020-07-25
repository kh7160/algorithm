# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = input()
    table = [list(map(int, input().split())) for _ in range(100)]
    pivot = [[table[j][i] for j in range(100)] for i in range(100)]
    max = 0
    for i in range(100):
        max = sum(table[i]) if max < sum(table[i]) else max
        max = sum(pivot[i]) if max < sum(pivot[i]) else max
    max = sum([table[i][i] for i in range(100)]) if max < sum([table[i][i] for i in range(100)]) else max
    print(f"#{case+1} {max}")