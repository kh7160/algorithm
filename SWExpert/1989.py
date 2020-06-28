# import sys
# sys.stdin = open("input.txt", "r")

t = int(input())
for i in range(t):
    test_case = input()
    is_valid = True
    for j in range(round(len(test_case)/2)):
        if test_case[j] == test_case[len(test_case)-j-1]:
            continue
        else:
            is_valid = False
            break

    print("#{} {}".format(i+1, 1 if is_valid == True else 0))
