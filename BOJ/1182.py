# import sys
# sys.stdin = open("input.txt", "r")

N, S = map(int, input().split())
num_list = list(map(int, input().split()))
temp = []
cnt = 0

def DFS(start):
    global cnt
    # print(start)
    if sum(temp) == S and len(temp) != 0:
        # print('correct')
        cnt += 1

    if start == N:
        return

    for i in range(start, N):
        # print('i : ' + str(i))
        temp.append(num_list[i])
        # print(temp)
        DFS(i+1)
        temp.pop()
        # print(temp)

DFS(0)
print(cnt)