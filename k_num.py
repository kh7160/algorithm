# def solution(array, commands):
#     answer = []
#     for it in range(len(commands)):
#         i = commands[it][0]
#         j = commands[it][1]
#         k = commands[it][2]
#
#         arr2 = array[i-1:j]
#         arr2.sort()
#         answer.append(arr2[k-1])
#
#     return answer

def solution(array, commands):
    return map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)

print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))