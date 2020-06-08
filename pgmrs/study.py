def solution(mylist):
    answer = [_ ** 2 for _ in mylist if _ % 2 == 0]
    return answer

print(solution([3,2,6,7]))