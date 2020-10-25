import itertools
n, m = map(int, input().split())
num_lst = [_+1 for _ in range(n)]
per_lst = list(itertools.permutations(num_lst,m))
for _ in per_lst:
    print(*_)