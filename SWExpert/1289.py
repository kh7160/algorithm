# import sys, time
# sys.stdin = open("input.txt", "r")

n = int(input())
for _ in range(n):
    origin = list(input())
    tmp = ['0'] * len(origin)
    idx = 0
    cnt = 0
    while True:
        if origin == tmp:
            break
        elif origin[idx] == tmp[idx]:
            pass
        else:
            tmp = tmp[:idx] + ['0' for _ in range(idx, len(origin))] if tmp[idx] == '1' else \
                  tmp[:idx] + ['1' for _ in range(idx, len(origin))]
            cnt += 1
        idx += 1
    print(f"#{_+1} {cnt}")