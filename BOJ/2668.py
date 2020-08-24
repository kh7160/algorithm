# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
lst = [0]*(n+1)
visited = [0]*(n+1)
for i in range(1,len(lst)):
    lst[i] = int(input())

def DFS(i):
    global is_cycled
    if (visited[i] == 1 and i == init_value):
        is_cycled = True
        return
    elif (visited[i] == 1 and i != init_value):
        return

    visited[i] = 1
    DFS(lst[i])
    if is_cycled == False:
        visited[i] = 0


for i in range(1,len(lst)):
    init_value = i
    is_cycled = False
    DFS(i)
    # print(i, visited)
print(visited.count(1))
result = [lst[i] for i in range(len(lst)) if visited[i] == 1]
result.sort()
print(*result, sep='\n')