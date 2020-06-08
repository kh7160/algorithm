def solution(clothes):
    answer = 1
    clothes_key = []
    clothes_nodup_key = {}
    clothes_cnt = []
    for _ in clothes:
        cloth_key = (lambda x: x[-1])(_)
        clothes_key.append(cloth_key)

    for _ in set(clothes_key):
        clothes_nodup_key[_] = clothes_key.count(_)
        clothes_cnt.append(clothes_key.count(_))

    for _ in clothes_cnt:
        answer *= _+1

    return answer-1



print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))
print(solution([['a', 'a'], ['a1', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd']]))