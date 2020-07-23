# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = int(input())
    table = [input().split() for _ in range(n)]
    cnt = 0
    for j in range(n):
        chk_pnt = []
        for i in range(n):
            if table[i][j] == '1':
                for k in range(i+1,n):
                    if table[k][j] == '2':
                        if k not in chk_pnt:
                            chk_pnt.append(k)
                            cnt += 1
                            break
                        else:
                            break
    print(f"#{case+1} {cnt}")