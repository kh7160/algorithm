import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input());
num = input().split();
arr = [0 for i in range(23)];

for i in range(len(num)):
    arr[int(num[i]) - 1] += 1;

for i in range(23):
    print(arr[i], end=' ');
