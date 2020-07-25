# import sys
# sys.stdin = open("input.txt", "r")

for case in range(10):
    n, lst = input().split()
    lst = list(lst)
    while True:
        len_list = len(lst)
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                del lst[i:i+2]
                break
        if len(lst) == len_list:
            break
    print("#{}".format(case+1), ''.join(lst))