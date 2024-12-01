class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit_set = set()
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0, 1)]

        def dfs(r, c):
            visit_set.add((r,c))
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if row in range(rows) and col in range(columns) and (row,col) not in visit_set and grid[row][col] == "1":
                    dfs(row,col)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visit_set:
                    dfs(r,c)
                    islands += 1

        return islands