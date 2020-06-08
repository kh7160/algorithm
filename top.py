def solution(heights):
    answer = []
    hei_len = len(heights)
    heights = heights[::-1]
    for i in range(hei_len):
        for j in range(i, hei_len):
            if heights[i] < heights[j]:
                answer.append(hei_len-j)
                break
            if j == hei_len-1:
                answer.append(0)
    answer = answer[::-1]
    return answer

print(solution([1,5,3,6,7,6,5]))