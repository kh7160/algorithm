n = list(map(int, input()))
n = sorted(n, reverse=True)
fnl = 0
try:
    n.index(0)
except:
    print(-1)
    exit(0)

if sum(n) % 3 != 0:
    print(-1)
else:
    for _ in n:
        fnl *= 10
        fnl += _
    print(fnl)