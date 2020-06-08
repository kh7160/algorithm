from queue import PriorityQueue

N = int(input())
arr = []
for _ in range(N):
    A, B = map(int, input().split())
    arr.append([A, B])

print(arr)
arr.sort(key=lambda x: x[0])
print(arr)
pque = PriorityQueue()
pque.put((arr[0][1], arr[0][1]))
for i in range(1, N):
    if pque.queue[0][1] <= arr[i][0]:
        pque.get()
        pque.put((arr[i][1], arr[i][1]))
    else:
        pque.put((arr[i][1], arr[i][1]))
print(pque.qsize())