def recur_func(n, i, box):
    global white, blue
    white_cnt, blue_cnt = 0, 0
    # print(n, i, box)
    for _ in box:
        # print(_)
        if _ == list('0' * n):
            white_cnt += 1
        elif _ == list('1' * n):
            blue_cnt += 1
        else:
            break

    if white_cnt == n:
        white += 1
        return
    elif blue_cnt == n:
        blue += 1
        return

    recur_func(n // 2, i + 1, [_[:n // 2] for _ in box[:n // 2]])
    recur_func(n // 2, i + 1, [_[:n // 2] for _ in box[n // 2:]])
    recur_func(n // 2, i + 1, [_[n // 2:] for _ in box[:n // 2]])
    recur_func(n // 2, i + 1, [_[n // 2:] for _ in box[n // 2:]])

n = int(input())
box = [input().split(' ') for _ in range(n)]
white, blue = 0, 0

recur_func(n, 1, box)
print(white)
print(blue)
