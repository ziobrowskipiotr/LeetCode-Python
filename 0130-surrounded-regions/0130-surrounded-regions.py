#1
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        rows = len(board)
        columns = len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(row, col):
            board[row][col] = "T"
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r in range(rows) and c in range(columns) and board[r][c] == "O":
                    dfs(r, c)


        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][columns-1] == "O":
                dfs(row, columns-1)

        for col in range(columns):
            if board[0][col] == "O":
                dfs(0, col)
            if board[rows-1][col] == "O":
                dfs(rows-1, col)
        
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"