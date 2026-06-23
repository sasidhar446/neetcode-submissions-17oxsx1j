class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, islands = len(grid), len(grid[0]), 0

        def bfs(r, c):
            deq = deque()
            deq.append((r, c))

            while deq:
                r, c = deq.popleft()
                grid[r][c] = '0'

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        deq.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        
        return islands
        
