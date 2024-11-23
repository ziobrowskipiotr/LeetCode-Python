class Solution:
    def solveNQueens(self, n: int) -> int:
        col = set() # columns
        pos_diag = set() # rows + columns
        neg_diag = set() # rows - columns
        result = [["." for i in range(n)] for i in range(n)]
        return_list = []
        def backtrack(row):
            if row == n:
                return_list.append(["" for i in range(n)])
                for i in range(n):
                    for j in range(n):
                        return_list[-1][i] += result[i][j]
                return
            else:
                for c in range(n):
                    if c not in col and row-c not in neg_diag and row+c not in pos_diag:
                        col.add(c)
                        neg_diag.add(row-c)
                        pos_diag.add(row+c)
                        result[row][c] = "Q"
                        backtrack(row+1)
                        col.remove(c)
                        neg_diag.remove(row-c)
                        pos_diag.remove(row+c)
                        result[row][c] = "."
                    elif c == n-1:
                        return
                    else:
                        continue
        backtrack(0)
        return return_list
		