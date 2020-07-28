n = int(input())
chk = 0
def brute_force(num):
    if num == 0:
        return 0
    return num % 10 + brute_force(num // 10)

for i in range(n):
    if brute_force(i) + i == n:
        print(i)
        chk = 1
        break

if chk != 1:
    print(0)