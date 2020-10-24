n = int(input())
cdhd_lst = []
for _ in range(n):
    age, name = input().split()
    cdhd_lst.append([int(age), name, _])
cdhd_lst.sort(key=lambda x:(x[0], x[2]))
for _ in cdhd_lst:
    print(_[0], _[1])