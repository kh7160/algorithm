# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    speed = 0
    length = 0

    for i in range(n):
        line = input().split(' ')
        if line[0] == '0':
            length += speed
        elif line[0] == '1':
            speed += int(line[1])
            length += speed
        else:
            if speed - int(line[1]) < 0:
                speed = 0
            else:
                speed -= int(line[1])
            length += speed
    print(f"#{case+1} {length}")
