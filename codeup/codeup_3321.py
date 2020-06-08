n = int(input())
a, b = map(int, input().split(' '))
c = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
max = 0

arr.sort()
arr = arr[::-1]
max = c // a
tot = c
for i in range(n):
    tot += arr[i]
    if max < (tot // (a + b * (i + 1))):
        max = (tot // (a + b * (i + 1)))

print(max)