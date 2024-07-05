# Print Board
def print_board(board):
    for row in board:
        for it in row:
            print(it, end=" ")
        print(" ")

# Check if the given Number can be placed at the given position
def is_vaild(k, row, col, board):
    row, col = int(row), int(col)
    for i in range(9):
        if board[row][i] == k:
            return False
        if board[i][col] == k:
            return False
        if board[3 * int(row / 3) + int(i / 3)][3 * int(col / 3) + int(i % 3)] == k:
            return False
    return True

# Backtracking Algorithm to solve Sudoku
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    if is_vaild(str(k), i, j, board):
                        board[i][j] = str(k)
                        if solve(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False
    return True

