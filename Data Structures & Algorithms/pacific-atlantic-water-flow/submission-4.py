class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited, atlantic_visited = set(), set()
        pacific_deq = collections.deque()
        atlantic_deq = collections.deque()
        rows, cols, result = len(heights), len(heights[0]), []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_deq.append((r, c))
                    pacific_visited.add((r, c))
                if r == rows - 1 or c == cols - 1:
                    atlantic_deq.append((r, c))
                    atlantic_visited.add((r, c))

        def bfs(deq, visited):
            while deq:
                r, c = deq.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                        if (nr, nc) not in visited:
                            deq.append((nr, nc))
                            visited.add((nr, nc))
        
        bfs(pacific_deq, pacific_visited)
        bfs(atlantic_deq, atlantic_visited)

        for cell in atlantic_visited:
            if cell in pacific_visited:
                result.append(cell)

        return result
