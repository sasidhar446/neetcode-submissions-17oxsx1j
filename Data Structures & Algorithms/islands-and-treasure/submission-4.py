class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        deq = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    deq.append((r, c))
        
        while deq:
            r, c = deq.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    deq.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
                    
        
                    