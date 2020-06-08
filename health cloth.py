# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#     answer = 0
#
#     lost2 = set(lost) - set(reserve)
#     reserve2 = set(reserve) - set(lost)
#
#     lost = list(lost2)
#     reserve = list(reserve2)
#
#     for i in range(len(lost)):
#         lp = lost[i]
#         for j in range(len(reserve)):
#             if reserve[j]-1 == lp or reserve[j]+1 == lp or reserve[j] == lp:
#                 answer += 1
#                 del reserve[j]
#                 break
#     answer += n - len(lost)
#     return answer

def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    print(_reserve)
    print(_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

print(solution(5, [1,2], [2,3]))

lst = [[col for col in range(0,10) if col % 2 == 0] for row in range(0,10)]
print(lst)