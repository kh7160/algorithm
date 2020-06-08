def solution(seoul):
    ix = seoul.index("Kim")
    answer = '김서방은 ' + str(ix) + '에 있다'
    return answer

print(solution(["Jane", "Kim"]))