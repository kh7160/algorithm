import collections
# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):
    line = collections.deque(sorted(map(int, input().strip().split(' '))))
    line.popleft()
    line.pop()
    print("#{} {}".format(i+1, round(sum(line) / len(line))))
