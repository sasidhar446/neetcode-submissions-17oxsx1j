class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        def bfs(r, c):
            deq = collections.deque()
            deq.append((r, c))
            island_area = 0

            while deq:
                r, c = deq.popleft()

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    island_area += 1
                    grid[r][c] = 0
                    for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        deq.append((nr + r, nc + c))
            
            return island_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = bfs(r, c)
                    area = max(area, island_area)
        
        return area
        