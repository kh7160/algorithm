import sys
sys.stdin = open("input.txt", "r")

tot = int(input())
a_lst = []
b_lst = []
tot_cnt = [0] * (tot + 1)

while True:
    a, b = map(int, input().split(' '))
    if a == -1 and b == -1:
        break
    a_lst.append(a)
    b_lst.append(b)

def DFS(a, i, cnt):
    if visited[a] == 1:
        return cnt - 1
    visited[a] = 1
    cnt += 1
    idx = a_lst.index(b_lst[i])
    return DFS(a_lst[idx], idx, cnt)

print(a_lst, b_lst)
for i in range(len(a_lst)):
    visited = [0] * (tot + 1)
    cnt = 0
    tot_cnt[a_lst[i]] = DFS(a_lst[i], i, cnt)

print(tot_cnt)
print(min(tot_cnt[1:]))
print(tot_cnt.count(min(tot_cnt[1:])))
print([i for i in range(len(tot_cnt[1:])+1) if tot_cnt[i] == min(tot_cnt[1:])])