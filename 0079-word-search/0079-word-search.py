class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(word_i, board_i, board_j):
            if board[board_i][board_j] == word[word_i]:
                if word_i == len(word) - 1:
                    return True
                else:
                    if board_j != 0:
                        if board[board_i][board_j - 1] != "0":
                            temp = board[board_i][board_j]
                            board[board_i][board_j] = "0"
                            if backtrack(word_i + 1, board_i, board_j - 1):
                                return True
                            board[board_i][board_j] = temp
                    if board_j != len(board[0]) - 1:
                        if board[board_i][board_j + 1] != "0":
                            temp = board[board_i][board_j]
                            board[board_i][board_j] = "0"
                            if backtrack(word_i + 1, board_i, board_j + 1):
                                return True
                            board[board_i][board_j] = temp
                    if board_i != 0:
                        if board[board_i - 1][board_j] != "0":
                            temp = board[board_i][board_j]
                            board[board_i][board_j] = "0"
                            if backtrack(word_i + 1, board_i - 1, board_j):
                                return True
                            board[board_i][board_j] = temp
                    if board_i != len(board) - 1:
                        if board[board_i + 1][board_j] != "0":
                            temp = board[board_i][board_j]
                            board[board_i][board_j] = "0"
                            if backtrack(word_i + 1, board_i + 1, board_j):
                                return True
                            board[board_i][board_j] = temp
                    return False
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True
        return False
