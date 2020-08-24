# import sys
# sys.stdin = open("input.txt", "r")

import copy
square = []
for _ in range(100):
    square.append(copy.deepcopy([0]*100))
input_lst = []
for _ in range(4):
    input_lst.append(list(map(int, input().split(' '))))

for _next in input_lst:
    a = (_next[0], _next[1])
    b = (_next[2], _next[3])
    for i in range(a[1], b[1]):
        # print(a[0], b[0])
        square[i][a[0]:b[0]] = [1] * (b[0]-a[0])

print(sum([line.count(1) for line in square]))