import sys
sys.stdin = open("input.txt", "r")

t = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for case in range(t):
    money_map = [0, 0, 0, 0, 0, 0, 0, 0]
    n = int(input())
    for i in range(len(money)):
        if n // money[i] != 0:
            money_map[i] = n // money[i]
            n -= money_map[i] * money[i]
        else:
            money_map[i] = 0
    print(f"#{case+1}")
    print(*money_map)