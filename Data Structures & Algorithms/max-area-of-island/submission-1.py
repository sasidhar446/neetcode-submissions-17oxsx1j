class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            current_area = 1

            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                 current_area += dfs(nr + r, nc + c)
            
            return current_area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = dfs(r, c)
                    area = max(area, island_area)
        
        return area
        