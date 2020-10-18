n = int(input())
fnl_num = '666'
cnt = 0
num = 0
while True:
    num += 1
    if str(num).find(fnl_num) != -1:
        cnt += 1
        if cnt == n:
            break

print(num)