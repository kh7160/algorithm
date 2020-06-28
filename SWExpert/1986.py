# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):
    n = int(input())
    print("#{} {}".format(i+1, sum([_ if _ % 2 != 0 else \
                          -1*_ for _ in range(1,n+1)])))