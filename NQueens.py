n=int(input("Enter the size of the board: "))
def solveNQueens(board,col):
    if col==n:
        for i in board:
            print(i)
        return True
    for i in range(n):
        if isSafe(board,i,col):
            board[i][col]=1
            if solveNQueens(board,col+1):
                return True
            board[i][col]=0
    return False
def isSafe(board,row,col):
    for x in range(col):
        if board[row][x]==1:
            return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    for x,y in zip(range(row,n),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    return True
board=[[0 for x in range(n)] for y in range(n)]

if not solveNQueens(board,0):
    print("No Solution")
