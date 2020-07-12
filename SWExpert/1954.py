import sys, math
sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    init = 1
    tmp_lst = [[0 for _ in range(n)] for _ in range(n)]
    tmp_len = n
    for i in range(math.ceil(n/2)):
        tmp_len -= 1
        if i == tmp_len:
            tmp_lst[i][tmp_len] = init
            break

        for j in range(i,tmp_len):
            tmp_lst[i][j] = init
            init += 1
        for j in range(i,tmp_len):
            tmp_lst[j][tmp_len] = init
            init += 1
        for j in range(tmp_len,i,-1):
            tmp_lst[tmp_len][j] = init
            init += 1
        for j in range(tmp_len,i,-1):
            tmp_lst[j][i] = init
            init += 1

    print(f"#{case + 1}")
    for i in range(len(tmp_lst)):
        for j in range(len(tmp_lst[i])):
            print(tmp_lst[i][j], end=' ')
        print('')