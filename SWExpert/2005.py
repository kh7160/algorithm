import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for _ in range(t):
    n = int(input())

    pascal = []
    for i in range(n):
        pascal.append([1 if _ == 0 or _ == i else\
                       pascal[i-1][_-1] + pascal[i-1][_] for _ in range(i+1)])

    print('#{}'.format(_ + 1))
    for i in pascal:
        print(' '.join(map(str, i)))