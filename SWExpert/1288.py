# import sys, time
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    cnt = 1
    lst = set()
    while True:
        comp = str(n * cnt)
        lst = lst | set(list(comp))
        if len(lst) == 10:
            break
        cnt += 1
    print(f"#{case+1} {comp}")