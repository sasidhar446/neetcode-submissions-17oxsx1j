class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols, fresh, minutes = len(grid), len(grid[0]), 0, 0
        deq = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    deq.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        while deq and fresh > 0:
            deqlen = len(deq)
            for _ in range(deqlen):
                r, c = deq.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        deq.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            minutes += 1

        
        return minutes if fresh == 0 else -1
            


 