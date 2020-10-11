n = int(input())
tot = []
fnl_grd = []
for _ in range(n):
    tot.append(tuple(map(int,input().split())))

for i in range(n):
    grd = 1
    for j in range(n):
        if tot[i][0] < tot[j][0] and tot[i][1] < tot[j][1]:
            grd += 1
    fnl_grd.append(grd)

print(*fnl_grd)