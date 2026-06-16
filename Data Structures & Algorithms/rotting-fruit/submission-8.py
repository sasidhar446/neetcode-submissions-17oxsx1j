class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        deq = collections.deque()
        count, fresh_apples = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    deq.append((r, c))
                if grid[r][c] == 1:
                    fresh_apples += 1

        if fresh_apples == 0: return 0

        while deq:
            deqLen = len(deq)
            for _ in range(deqLen):
                r, c = deq.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        deq.append([nr, nc])
                        grid[nr][nc] = 2
                        fresh_apples -= 1
            if deq:
                count += 1

        return -1 if fresh_apples != 0 else count
