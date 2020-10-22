n = int(input())
num_lst = [list(map(int, input().split())) for _ in range(n)]
num_lst.sort(key=lambda x:(x[1], x[0]))
for _ in num_lst:
    print(*_)