class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit_set = set()
        neighbors = collections.deque()
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0, 1)]

        def bfs(r, c):
            visit_set.add((r,c))
            neighbors.append((r,c))
            while neighbors:
                row, col = neighbors.popleft()
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(columns) and (r,c) not in visit_set and grid[r][c] == "1":
                        visit_set.add((r,c))
                        neighbors.append((r,c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visit_set:
                    bfs(r,c)
                    islands += 1

        return islands