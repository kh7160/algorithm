import math
def solution(brown, yellow):
    answer = []
    col_max = int(math.sqrt(yellow))
    # print(col_max)
    for i in range(1,col_max+1):
        if yellow % i == 0:
            y_row = yellow // i
            y_col = yellow // y_row
            b_row = y_row + 2
            b_col = y_col + 2
            # print(y_col, y_row, b_col, b_row)
            if b_row * b_col - y_row * y_col == brown:
                answer = [b_row, b_col]

    return answer

print(solution(24,24))