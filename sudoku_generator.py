# sudoku_generator.py
import random


def is_valid(board, row, col, num):
    # 检查行是否合法
    if num in board[row]:
        return False

    # 检查列是否合法
    if num in [board[i][col] for i in range(9)]:
        return False

    # 检查3x3子网格是否合法
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_sudoku():
    # 创建一个9x9的空数独谜题
    board = [[0 for _ in range(9)] for _ in range(9)]

    # 使用回溯算法解决空数独谜题
    solve_sudoku(board)

    # 随机挖洞，生成题目
    num_holes = random.randint(40, 60)  # 谜题难度可以根据挖洞数量调整
    for _ in range(num_holes):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board
