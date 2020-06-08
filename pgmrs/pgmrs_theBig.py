def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    answer = ''.join(numbers)
    return answer

print(solution([1,10,100]))