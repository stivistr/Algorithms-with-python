def gen_func(idx, board):
    if idx >= len(board):
        print(*board, sep='')
        return
    for num in range(2):
        board[idx] = num
        gen_func(idx + 1, board)


n = int(input())
vector_board = [0] * n
gen_func(0, vector_board)
