# import sys
# sys.stdin = open("input.txt", "r")
tmp_lst = []

def num_list(num):
    global cnt
    if num == n:
        cnt += 1
        return
    elif num > n:
        return

    for i in range(1,4):
        num_list(num + i)

tot = int(input())
for case in range(tot):
    n = int(input())
    cnt = 0
    num_list(0)
    print(cnt)