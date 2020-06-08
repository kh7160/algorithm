def solution(board, moves):
    stack = []
    row, col = len(board), len(board[0])
    del_doll = 0
    print(row, col)
    for i in range(len(moves)):
        move = moves[i]
        print(board)
        for j in range(row):
            if board[j][move-1] > 0:
                stack.append(board[j][move-1])
                board[j][move-1] = 0
                break
        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                del stack[len(stack)-1]
                del stack[len(stack)-1]
                del_doll += 2
        print(stack)
    answer = del_doll
    return answer