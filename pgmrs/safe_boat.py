def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    j = len(people) - 1

    for i in range(len(people)):
        if i > j:
            break

        if people[i] + people[j] <= limit:
            j -= 1
        answer += 1

    return answer

print(solution([70, 50, 50, 80], 100))