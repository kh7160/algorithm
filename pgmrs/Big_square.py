import numpy as np

def solution(board):
    answer = 1
    board = np.array(board)
    row = len(board)
    col = len(board[0])
    max = 1
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                end_col = 1
                for k in range(j+1, col):
                    if board[i][k] == 1:
                        end_col += 1
                    else:
                        break
                print(i, j, end_col)
                print(board[i][j:j+end_col])
                # print(board[i:i+end_col])
                print(board[i:i+end_col, j:j+end_col])
                output = board[i:i+end_col, j:j+end_col]
                output = list(output)
                print(output.count(1))
    # print(max)
                # print(board[i:i+end_col])
    return answer

solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])