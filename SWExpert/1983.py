# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
score_dict = {}
for i in range(t):
    n, k = map(int, input().split(' '))
    for j in range(n):
        mid, fnl, report = map(int, input().split(' '))
        score_dict[j] = mid*0.35 + fnl*0.45 + report*0.2
    # print(score_dict)
    sort_dict = dict(sorted(score_dict.items(), key=lambda x:x[1], reverse=True))
    dict_key = list(sort_dict.keys())
    dict_value = list(sort_dict.values())
    # print(dict_key, dict_value)
    # print(dict_key.index(k-1), dict_value[dict_key.index(k-1)])
    rank = dict_key.index(k-1) + 1
    # print(rank, rank/n)
    print("#{} {}".format(i+1, 'A+' if rank / n <= 0.1 else \
                               'A0' if rank / n <= 0.2 else \
                               'A-' if rank / n <= 0.3 else \
                               'B+' if rank / n <= 0.4 else \
                               'B0' if rank / n <= 0.5 else \
                               'B-' if rank / n <= 0.6 else \
                               'C+' if rank / n <= 0.7 else \
                               'C0' if rank / n <= 0.8 else \
                               'C-' if rank / n <= 0.9 else \
                               'D0' if rank / n <= 1.0 else None))