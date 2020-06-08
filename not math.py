def solution(answers):
    one_person = [1,2,3,4,5]
    two_person = [2, 1, 2, 3, 2, 4, 2, 5]
    third_person = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    right1, right2, right3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one_person[i % len(one_person)]:
            right1 += 1
        if answers[i] == two_person[i % len(two_person)]:
            right2 += 1
        if answers[i] == third_person[i % len(third_person)]:
            right3 += 1

    max_answer = max(right1, right2, right3)
    answer = []
    if max_answer == right1:
        answer.append(1)
    if max_answer == right2:
        answer.append(2)
    if max_answer == right3:
        answer.append(3)
    return answer

print(solution([1,3,2,4,2]))