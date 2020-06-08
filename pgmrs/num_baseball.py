import itertools

def solution(baseball):
    all_num = list(map(''.join, itertools.permutations(['1','2','3','4','5','6','7','8','9'], 3)))
    baseball.sort(key = lambda x:x[1], reverse=True)
    result = all_num
    for num, strike, ball in baseball:
        tmp = []
        for i in range(len(all_num)):
            if check_num(all_num[i], str(num), strike, ball) == True:
                tmp.append(all_num[i])
        # print(result)
        result = set(result) & set(tmp)
        result = list(result)
    answer = len(result)
    return answer

def check_num(all_num, num, strike, ball):
    strike2 = 0
    ball2 = 0
    for i in range(3):
        if all_num[i] == num[i]:
            strike2 += 1
        if all_num[i] in num:
            ball2 += 1
    if strike == strike2 and ball == (ball2 - strike2):
        return True

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))