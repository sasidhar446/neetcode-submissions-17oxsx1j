class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            deq = collections.deque()
            deq.append((r, c))
            island_area = 1
            grid[r][c] = 0

            while deq:
                r, c = deq.popleft()

                for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = nr + r, nc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        deq.append((nr, nc))
                        island_area += 1
                        grid[nr][nc] = 0

            return island_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = bfs(r, c)
                    area = max(area, island_area)
        
        return area
        