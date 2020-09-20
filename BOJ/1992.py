def recur_func(n, tot):
    white_cnt, black_cnt = 0, 0
    for _ in tot:
        if _.count('0') == n:
            white_cnt += 1
        elif _.count('1') == n:
            black_cnt += 1
    if white_cnt == n:
        print('0', end='')
        return
    elif black_cnt == n:
        print('1', end='')
        return

    print('(', end='')
    recur_func(n // 2, [_[:n // 2] for _ in tot[:n // 2]])
    recur_func(n // 2, [_[n // 2:] for _ in tot[:n // 2]])
    recur_func(n // 2, [_[:n // 2] for _ in tot[n // 2:]])
    recur_func(n // 2, [_[n // 2:] for _ in tot[n // 2:]])
    print(')', end='')

n = int(input())

tot = [list(input()) for _ in range(n)]
recur_func(n, tot)
