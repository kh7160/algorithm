import collections

def solution(priorities, location):
    answer = 0
    deq = collections.deque(priorities)
    while deq:
        max_pop = max(deq)
        pop = deq.popleft()
        location -= 1

        if pop >= max_pop:
            answer += 1
            if location == -1:
                return answer
            continue
        else:
            deq.append(pop)
            if location == -1:
                location = len(deq)-1
    return answer

print(solution([2,1,3,2], 2))

# deq = collections.deque([2,1,3,2])
# pop = deq.popleft()
# print(pop)
# print(deq)