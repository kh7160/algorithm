def solution(name):
    answer = 0
    ix = 0
    name = list(name)
    right = 0
    left = 0
    while True:
        print('name : ', name[ix])
        if name[ix] != 'A':
            ix1 = ord(name[ix]) - ord('A')
            ix2 = ord('Z') - ord(name[ix]) + 1
            answer += ix1 if ix1 <= ix2 else ix2
        name[ix] = 'A'
        if ''.join(name) == 'A' * len(name):
            return answer
        for i in range(1, len(name)):
            if name[ix + i] == "A":
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[ix - i] == "A":
                left += 1
            else:
                break
    # for j in range(1,len(name)):
    #         if(name[ix + j if ix + j < len(name) else ix + j - len(name)] != 'A'):
    #             right = j
    #             left = len(name)
    #             break
    #         if (name[ix - j] != 'A'):
    #             left = j
    #             right = len(name)
    #             break
        answer += right if right <= left else left
        ix = ix + right if right <= left else i
    return answer

print(solution("JAN"))
# abcdefghijklnmopqrstuvwxyz