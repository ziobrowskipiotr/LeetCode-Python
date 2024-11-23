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
                    if c not in col and row-c not in neg_diag and row+c not in pos_diag:
                        col.add(c)
                        neg_diag.add(row-c)
                        pos_diag.add(row+c)
                        backtrack(row+1)
                        col.remove(c)
                        neg_diag.remove(row-c)
                        pos_diag.remove(row+c)
                    elif c == n-1:
                        return
                    else:
                        continue
        backtrack(0)
        return result
		