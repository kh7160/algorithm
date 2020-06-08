n, k = input().split(' ')
n, k = int(n), int(k)
arr = []
answer = 0
arr_ix = 0
for i in range(int(n)):
    arr.append(int(input()))

arr = arr[::-1]
while k != 0:
    if k >= arr[arr_ix]:
        answer += k // arr[arr_ix]
        k %= arr[arr_ix]
    else:
        arr_ix += 1

print(answer)