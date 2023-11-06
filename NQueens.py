

n = int(input("Enter the size of the board: "))

def solveNQueens(board, col, solutions):
    if col == n:
        solution = [" ".join(row) for row in board]
        solutions.append(solution)
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 'Q'
            solveNQueens(board, col+1, solutions)
            board[i][col] = '0'

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 'Q':
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 'Q':
            return False
    for x, y in zip(range(row, n), range(col, -1, -1)):
        if board[x][y] == 'Q':
            return False
    return True

board = [['0' for x in range(n)] for y in range(n)]
solutions = []

solveNQueens(board, 0, solutions)

if not solutions:
    print("No Solution")
else:
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print("\n")

