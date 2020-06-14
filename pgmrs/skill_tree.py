def solution(skill, skill_trees):
    answer = 0
    for _ in skill_trees:
        tmp = ''
        tmp_check = True
        for i in range(len(_)):
            if _[i] in skill:
                tmp += _[i]

        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                tmp_check = False

        if tmp_check == True:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))