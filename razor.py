# def solution(arrangement):
#     answer = 0
#     pre = ''
#     arr = []
#     for i in arrangement:
#         if i == '(':
#             arr.append(i)
#             pre = i
#         else:
#             if pre == '(':
#                 arr.pop()
#                 answer += len(arr)
#                 pre = i
#             else:
#                 arr.pop()
#                 pre = i
#                 answer += 1
#     return answer
#
def solution(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')
    print(rasor_to_zero)
    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer

solution('()(((()())(())()))(())')