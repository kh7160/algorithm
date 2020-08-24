# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
page_lst = [sorted(map(int, input().split(' '))) for _ in range(n)]
# print(page_lst)
cnt = [0]*n

def stack(i):
    if cnt[i]:
        return cnt[i]
    cnt[i] = 1
    for j in range(n):
        if i != j and (page_lst[i][0] >= page_lst[j][0] and page_lst[i][1] >= page_lst[j][1]):
            cnt[i] = max(cnt[i], stack(j)+1)

    return cnt[i]

for i in range(n):
    cnt[i] = stack(i)

# print(cnt)
print(max(cnt))