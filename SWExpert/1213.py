# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n = int(input())
    word = input()
    line = input()

    print("#{} {}".format(case+1, line.count(word)))