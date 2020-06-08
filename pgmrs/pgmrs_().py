def solution(s):
    idx = 0
    chk = 0

    while idx != len(s):
        answer = False
        if s[idx] == '(':
            for _ in s[idx:]:
                if _ == '(':
                    chk += 1
                    idx += 1
                else:
                    chk -= 1
                    idx += 1

                if chk == 0:
                    answer = True
                    break

        else:
            return False

    return answer

print(solution("()()()("))