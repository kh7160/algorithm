arr = []
pasta_min = 2000
juice_min = 2000
for _ in range(5):
    arr.append(int(input()))

for _ in range(3):
    if pasta_min > arr[_]:
        pasta_min = arr[_]

for _ in range(3,5):
    if juice_min > arr[_]:
        juice_min = arr[_]

num = (pasta_min + juice_min) * 1.1
print('%.1f' % num)