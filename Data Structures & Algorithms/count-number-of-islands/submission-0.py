class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            deq = collections.deque()
            deq.append((r, c))

            while deq:
                r, c = deq.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for nr, nc in directions:
                    nr, nc = nr + r, nc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        deq.append((nr, nc))
                        grid[nr][nc] = "0"


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    bfs(r, c)
        
        return island_count
        