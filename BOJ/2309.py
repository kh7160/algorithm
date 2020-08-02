import sys
sys.stdin = open("input.txt", "r")

small_men = []
tmp = []
for _ in range(9):
    small_men.append(int(input()))

# print(small_men)
def brute_force(num):
    print(tmp)
    if len(tmp) == 7:
        if sum(tmp) == 100:
            tmp.sort()
            for _ in tmp:
                print(_)
        return

    for i in range(num, 9):
        tmp.append(small_men[i])
        print('=================' + '재귀 전' + '=================')
        brute_force(i+1)
        print('=================' + '재귀 후' + '=================')
        tmp.pop()

brute_force(0)