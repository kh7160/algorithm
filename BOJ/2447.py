def recur_func(star):
    result = []
    for i in range(3 * len(star)):
        if i // len(star) == 1:
            result.append(star[i%len(star)] + ' ' * len(star) + star[i%len(star)])
        else:
            result.append(star[i%len(star)] * 3)
    return result

star = ['***', '* *', '***']
n = int(input())
cnt = 0
while n != 3:
    n //= 3
    cnt += 1

for i in range(cnt):
    star = recur_func(star)

for _ in star:
    print(_)