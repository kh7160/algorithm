a, b = map(int, input().split(' '))
cnt = 0
while True:
    if b - a == 0:
        print(cnt)
        break

    if abs(b - a) >= 8:
        if b - a > 0:
            a += 10
        else:
            a -= 10
        cnt += 1
    elif abs(b - a) >= 3:
        if b - a > 0:
            a += 5
        else:
            a -= 5
        cnt += 1
    else:
        if b - a > 0:
            a += 1
        else:
            a -= 1
        cnt += 1