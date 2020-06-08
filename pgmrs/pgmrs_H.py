def solution(citations):
    citations.sort(reverse=True)
    # print(citations)
    max = 0
    for i in range(len(citations)):
        cnt = 0
        for j in range(i, -1, -1):
            if citations[j] >= citations[i]:
                cnt += 1
        # print(max, cnt, citations[i])
        if max < cnt and citations[i] >= cnt:
            max = cnt
    return max

# print(solution([3,0,6,1,5]))
print(solution([0,1,1,1,1,3,3,4]))