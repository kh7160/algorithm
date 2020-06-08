def solution(n, m):
    max, min = 1, 1
    for i in range(1, n+1):
        if m % i == 0 and n % i == 0:
            max = i

    for i in range(1, int(10000000 / n)):
        if (n * i) % m == 0:
            min = n * i
            break
    answer = []
    answer.append(max)
    answer.append(min)
    return answer

print(solution(10,10))