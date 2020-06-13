from collections import deque

def solution(people, limit):
    answer = 0
    # people.sort()
    people_deque = deque(sorted(people))
    while people_deque:
        init = people_deque.popleft()
        sum_max = 0
        max_i = -1
        for i in range(len(people_deque)):
            if init + people_deque[i] > limit:
                break
            if init + people_deque[i] > sum_max:
                sum_max = init + people_deque[i]
                max_i = i

        if max_i != -1:
            del people_deque[max_i]

        answer += 1

    return answer

print(solution([70, 50, 50, 30], 100))