n = int(input())
arr = []
tmp = []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr)
tmp_max = 0
for i in range(n):
    tmp.append(arr.pop())
    tmp_max = max(tmp_max, tmp[i] * (i+1))

print(tmp_max)