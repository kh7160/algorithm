# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for case in range(t):
    n = int(input())
    case_dict = {}
    for i in range(n):
        lst = input().split(' ')
        case_dict[lst[0]] = int(lst[1])
    cnt = 0
    print('#{}'.format(case+1))
    # print(case_dict)
    for i in case_dict:
        for j in range(case_dict[i]):
            print(i, end='')
            cnt += 1
            if cnt % 10 == 0:
                print('')
                cnt = 0
    print('')