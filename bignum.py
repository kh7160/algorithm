def solution(number, k):
    answer = ''
    arr = []
    chkpnt = 0
    for _ in number:
        while arr and arr[-1] < _:
            arr.pop()
            k -= 1
            if k == 0:
                break

        if k == 0:
            break
        arr.append(_)
        chkpnt += 1
    if len(arr) > len(number) - k:
        return ''.join(arr[:len(number)-k])
    answer += ''.join(arr) + number[chkpnt:]
    return answer


print(solution("77777777", 2))
