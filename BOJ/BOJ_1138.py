n = int(input())
arr = list(map(int, input().split(' ')))
res = [0] * n
for i in range(n):
    ix = arr[i]
    cnt = 0
    for j in range(n):
        if res[j] == 0 and ix == cnt:
            res[j] = i+1
            break
        if res[j] == 0:
            cnt+=1

for i in res:
    print(i, end=' ')