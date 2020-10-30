import itertools
n,m = map(int, input().split())
num_lst = [_+1 for _ in range(n)]
num_lst = list(itertools.product(num_lst, repeat=m))
for _ in num_lst:
    print(*_)