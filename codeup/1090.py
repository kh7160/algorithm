import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

a, r, n = map(int, input().split());
for i in range(n-1):
    a *= r;

print(a);