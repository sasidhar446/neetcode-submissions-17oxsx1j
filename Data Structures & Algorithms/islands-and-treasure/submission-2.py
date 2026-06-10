class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        deq = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    deq.append((r, c))
        
        while deq:
            r, c = deq.popleft()
            for nr, nc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r, next_c = nr + r, nc + c
                if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 2147483647:
                    deq.append((next_r, next_c))
                    grid[next_r][next_c] = grid[r][c] + 1