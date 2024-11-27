class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {}
        rows = {}
        squares = {}
        for i in range(9):
            columns[i] = set()
            rows[i] = set()
            squares[i] = set()

        def little_squares(i):
            if i<3:
                return 0
            elif i<6:
                return 1
            else:
                return 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                if board[i][j] in squares[3*little_squares(i)+little_squares(j)]:
                    return False
                else:
                    squares[3*little_squares(i)+little_squares(j)].add(board[i][j])
        return True