import sys
sys.stdin = open("input.txt", "r")

def get_point(num):
    cnt = 1
    rslt = tuple()
    for i in range(199):
        for j in range(i + 1):
            if cnt == num:
                rslt = (i - j + 1, j + 1)
            table[i - j + 1][j + 1] = cnt
            cnt += 1
    return rslt

t = int(input())
table = [[0 for _ in range(200)]for _ in range(200)]

for i in range(t):
    p, q = map(int, input().split())
    p_pnt = get_point(p)
    for _ in table:
        print(_)
    q_pnt = get_point(q)
    last_pnt = (p_pnt[0]+q_pnt[0], p_pnt[1]+q_pnt[1])
    print(p_pnt, q_pnt)
    print(last_pnt)
    print(f"#{i+1} {table[last_pnt[0]][last_pnt[1]]}")
