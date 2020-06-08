n = int(input())
arr = []
answer = 0
dup = 0
arr = sorted(list(map(int, input().split(' '))))
for i in arr:
    dup += i
    answer += dup

print(answer)