n = int(input())
for i in range(n):
    temp_sum = sum([_ for _ in list(map(int, input().split(' '))) if _ % 2 != 0])
    print(f"#{i+1} {temp_sum}")