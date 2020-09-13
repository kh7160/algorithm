import collections
import itertools

def solution(orders, course):
    answer = []
    for cnt in course:
        tmp = collections.Counter()
        for _ in orders:
            tmp += collections.Counter(list(itertools.combinations(_, cnt)))
        if len(tmp) == 0:
            break
        # print(tmp)
        max_grd = tmp.most_common()[0][1]
        for _ in [''.join(list(_)) for _ in [_[0] for _ in tmp.items() if _[1] == max_grd and _[1] >= 2]]:
            answer.append(_)
        answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))