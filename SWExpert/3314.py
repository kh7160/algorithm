# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    score_lst = map(int, input().split())
    print("#{} {}".format(case+1,int(sum([40 if _ < 40 else _ for _ in score_lst]) / 5)))