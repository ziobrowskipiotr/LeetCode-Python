class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set() # columns
        pos_diag = set() # rows + columns
        neg_diag = set() # rows - columns
        result = 0
        def backtrack(row):
            if row == n:
                nonlocal result
                result += 1
                return
            else:
                for c in range(n):
                    if c in col or row-c in neg_diag or row+c in pos_diag:
                        continue
                    else:
                        col.add(c)
                        neg_diag.add(row-c)
                        pos_diag.add(row+c)
                        backtrack(row+1)
                        col.remove(c)
                        neg_diag.remove(row-c)
                        pos_diag.remove(row+c)
        backtrack(0)
        return result
		