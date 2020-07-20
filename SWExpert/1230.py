import sys, time
sys.stdin = open("input.txt", "r")

for _ in range(10):
    origin_len = int(input())
    origin_lst = list(map(int, input().split()))
    n = int(input())
    order_lst = list(input().split())
    for i in range(n):
        clss = order_lst[0]
        if clss == 'I':
            loc = int(order_lst[1])
            num = int(order_lst[2])
            for j in range(num):
                origin_lst.insert(loc+j, int(order_lst[3+j]))
            del order_lst[0:3+num]
        elif clss == 'D':
            loc = int(order_lst[1])
            num = int(order_lst[2])
            del origin_lst[loc:loc+num]
            del order_lst[:3]
        elif clss == 'A':
            num = int(order_lst[1])
            for j in range(num):
                origin_lst.append(int(order_lst[2+j]))
            del order_lst[:2+num]
    print(f"#{_+1}", *origin_lst[:10])
