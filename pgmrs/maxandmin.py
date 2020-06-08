def solution(s):
    answer = ''
    num_list = list(map(int, s.split(' ')))
    answer += str(min(num_list)) + ' '
    answer += str(max(num_list))
    return answer

print(solution('-1 -1'))