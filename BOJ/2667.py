# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
map =[list(map(int,input())) for _ in range(n)]
map_chk = [[0]*n for _ in range(n)]
_next = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
cnt_lst = []
def DFS(x, y):
    if (x < 0 or x >= n) or (y < 0 or y >= n) or (map[x][y] == 0) or (map_chk[x][y] == 1):
        return

    if map[x][y] == 1:
        map_chk[x][y] = 1
        global cnt
        cnt += 1
        for k in range(4):
            DFS(x + _next[k][0], y + _next[k][1])
    return

for i in range(len(map)):
    for j in range(len(map[i])):
        cnt = 0
        DFS(i,j)
        if cnt > 0:
            cnt_lst.append(cnt)
cnt_lst.sort()
print(len(cnt_lst))
for _ in cnt_lst:
    print(_)