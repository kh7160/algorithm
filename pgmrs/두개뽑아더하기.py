def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        tmp = numbers[:i]
        tmp += numbers[i+1:]
        for j in tmp:
            answer.add(numbers[i]+j)
    answer = list(answer)
    answer.sort()
    return answer

print(solution([5,0,2,7]))