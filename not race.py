# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]
#
# participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
# completion = ['josipa', 'filipa', 'marina', 'nikola']
# print(solution(participant, completion))

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola', 'filipa']
print(solution(participant, completion))
