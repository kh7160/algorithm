import sys, collections
sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    score_lst = []
    n = int(input())
    line = list(map(int, input().split(' ')))
    # for i in range(101):
    #     score_lst.append(line.count(i))
    cnt = collections.Counter(line)
    print(cnt[])
    cnt = cnt.most_common()
    print(cnt)

    # print("#{} {}".format(n,score_lst.index(max(score_lst))))