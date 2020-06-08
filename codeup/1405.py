import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input());
num = input().split();

for i in range(n):
    for j in range(i, n + i):
        if(j >= n):
            print(num[j%n], end=' ');
        else:
            print(num[j], end=' ');
    print('');