class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols, max_area = len(grid), len(grid[0]), 0

        def bfs(r, c):
            deq = deque()
            deq.append((r, c))
            grid[r][c] = 0
            area = 1

            while deq:
                r, c = deq.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        deq.append((nr, nc))
                        grid[nr][nc] = 0
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(area, max_area)
        
        return max_area