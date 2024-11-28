class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        columns_len = len(board[0])-1
        rows_len = len(board)-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                actual_result = 0
                if j < columns_len:
                    actual_result += board[i][j+1] % 2
                if j > 0:
                    actual_result += board[i][j-1] % 2
                if i < rows_len:
                    actual_result += board[i+1][j] % 2
                if i > 0:
                    actual_result += board[i-1][j] % 2
                if j < columns_len and i < rows_len:
                    actual_result += board[i+1][j+1] % 2
                if i > 0 and j > 0:
                    actual_result += board[i-1][j-1] % 2
                if i > 0 and j < columns_len:
                    actual_result += board[i-1][j+1] % 2
                if i < rows_len and j > 0:
                    actual_result += board[i+1][j-1] % 2
                if board[i][j] == 1:
                    if actual_result < 2:
                        board[i][j] = 3
                    elif actual_result > 3:
                        board[i][j] = 3
                else:
                    if actual_result == 3:
                        board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
                    
                        
                        
        