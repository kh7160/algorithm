def solution(n):
    tmp = n
    n_tmp = bin(n)

    while True:
        tmp += 1
        b_tmp = bin(tmp)
        if n_tmp.count('1') == b_tmp.count('1'):
            return tmp

print(solution(15))