# import sys
# sys.stdin = open("input.txt", "r")

lst = []
for i in range(1,300):
    for j in range(i):
        lst.append((1+j,i-j))
print(lst)