def check(arr, size):
    global cnt0, cnt1, cnt2
    first = arr[0][0]
    for i in range(size):
        for j in range(size):
            if arr[i][j] != first:
                return False

    if first == '0':
        cnt0 += 1
    elif first == '1':
        cnt1 += 1
    else:
        cnt2 += 1

    return True

def recur_func(arr, size):
    global cnt0, cnt1, cnt2
    if check(arr, size):
        return
    # print(arr)
    size = size // 3
    for i in range(3):
        for j in range(3):
            # print([_[j*3:(j*3)+size] for _ in arr[i*3:(i*3)+size]])
            recur_func([_[j*size:(j*size)+size] for _ in arr[i*size:(i*size)+size]], size)
            # print(cnt0, cnt1, cnt2)
    return

cnt0, cnt1, cnt2 = 0, 0, 0 # 0 : 0, 1 : 1, 2 : -1
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().split())

recur_func(arr, n)
print(cnt2, cnt0, cnt1, sep='\n')