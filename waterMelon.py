def solution(n):
    answer = ''
    str = '수박'
    for i in range(n):
        answer += str[i%2]
    return answer

print(solution(3))