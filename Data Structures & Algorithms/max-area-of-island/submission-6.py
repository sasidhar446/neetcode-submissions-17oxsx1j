class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols, max_area = len(grid), len(grid[0]), 0
        self.area = 0

        def dfs(r, c):
            grid[r][c] = 0

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        self.area += 1
                        dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.area = 1
                    dfs(r, c)
                    max_area = max(self.area, max_area)
        
        return max_area