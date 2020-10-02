import itertools
def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    cnt = 1
    row, col = 0, 0
    for i in range(n):
        if i % 3 == 0:
            for j in range(i, n):
                answer[row][col] = cnt
                cnt += 1
                if j == n-1:
                    col += 1
                    break
                row += 1
        elif i % 3 == 1:
            for j in range(i, n):
                answer[row][col] = cnt
                cnt += 1
                if j == n-1:
                    row -= 1
                    col -= 1
                    break
                col += 1
        else:
            for j in range(i, n):
                answer[row][col] = cnt
                cnt += 1
                if j == n-1:
                    row += 1
                    break
                row -= 1
                col -= 1

    return list(itertools.chain(*answer))