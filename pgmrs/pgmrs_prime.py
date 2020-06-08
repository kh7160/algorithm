import itertools
import math
cnt = 0

def solution(numbers):
    global cnt
    result = set()
    for i in range(len(numbers)):
        tmp_result = list(map(int, list(map(''.join, itertools.permutations(numbers, i+1)))))
        for _ in tmp_result:
            result.add(_)
    # print(result)
    for _ in result:
        if isPrime(_) == True:
            cnt += 1
    return cnt

def isPrime(num):
    num = int(num)
    if num == 1 or num == 0:
        return False

    for i in range(2,num):
        n = int(math.sqrt(num))
        if i > num:
            break
        elif num % i == 0:
            return False
    # print(num)
    return True

print(solution('1234'))