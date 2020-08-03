# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
for _ in range(n):
    num = int(input())
    clss = False
    for i in range(1,47):
        for j in range(1,47):
            for k in range(1,47):
                if i * (i + 1) / 2 + j * (j + 1) / 2 + k * (k + 1) / 2 == num:
                    clss = True
                    break
            if clss == True:
                break
        if clss == True:
            break
    print(1 if clss == True else 0)