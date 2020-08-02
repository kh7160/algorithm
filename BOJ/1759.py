# import sys
# sys.stdin = open("input.txt", "r")

L, C = map(int, input().split())
alpha_lst = input().split()
alpha_lst.sort()
result_lst = []
moeum = ['a','e','i','o','u']
# print(alpha_lst)
def DFS(start, result_lst):
    moeum_cnt = 0
    jaeum_cnt = 0
    if len(result_lst) == L:
        # print(result_lst)
        for _ in result_lst:
            if _ in moeum:
                moeum_cnt += 1
            else:
                jaeum_cnt += 1
        if jaeum_cnt >= 2 and moeum_cnt >= 1:
            print(''.join(result_lst))
        return

    for i in range(start, C):
        result_lst.append(alpha_lst[i])
        DFS(i+1, result_lst)
        result_lst.pop()

DFS(0, result_lst)