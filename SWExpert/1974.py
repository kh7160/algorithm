# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
F = lambda arr,i,j:sum([sum([arr[_i][_j] for _i in range(i, i+3)]) for _j in range(j, j+3)])
for case in range(t):
    arr = [[_ for _ in map(int, input().split(' '))] for _ in range(9)]
    row_tot = [sum([arr[i][j] for j in range(9)]) for i in range(9)]
    col_tot = [sum([arr[i][j] for i in range(9)]) for j in range(9)]
    sqr_tot = [[F(arr, 0, 0) for i in range(0,9,3)] for j in range(0,9,3)]
    if row_tot.count(45) != 9 or col_tot.count(45) != 9 or sqr_tot.count([45, 45, 45]) != 3:
        print(f"#{case + 1} 0")
    else:
        print(f"#{case + 1} 1")