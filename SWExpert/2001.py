# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())

def hit_fly(fly_map, m):
    max = 0
    for i in range(len(fly_map) - m + 1):
        for k in range(len(fly_map) - m + 1):
            tmp = 0
            for j in range(k, k+m):
                tmp += sum(fly_map[j][i:i + m])
            # print(tmp)
            if tmp > max:
                max = tmp
    return max

for i in range(t):
    n, m = map(int, input().split(' '))
    fly_map = []
    for j in range(n):
        fly_map.append(list(map(int, input().split(' '))))

    print("#{} {}".format(i+1, hit_fly(fly_map, m)))
