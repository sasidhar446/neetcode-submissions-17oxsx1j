class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(r, c):
            deq = collections.deque()
            deq.append((r, c))
            grid[r][c] == '0'
            deqLen = len(deq)

            while deq:
                r, c = deq.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        deq.append((nr, nc))
                        grid[nr][nc] = '0'
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        
        return count
        
