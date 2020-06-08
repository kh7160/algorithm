import collections

def solution(A,B):
    answer = 0
    a = collections.deque(sorted(A))
    b = collections.deque(sorted(B, reverse=True))
    print(a, b)
    while 1:
        if len(a) == 0:
            break
        answer += (a.popleft() * b.popleft())

    return answer

print(solution([1,2],[3,4]))