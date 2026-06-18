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
                if r == rows - 1 or c == cols - 1:
                    atlantic_deq.append((r, c))
        
        while pacific_deq:
            r, c = pacific_deq.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in pacific_visited:
                        pacific_deq.append((nr, nc))
            
            pacific_visited.add((r, c))

        
        while atlantic_deq:
            r, c = atlantic_deq.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in atlantic_visited:
                        atlantic_deq.append((nr, nc))
            
            atlantic_visited.add((r, c))

        
        for cell in atlantic_visited:
            if cell in pacific_visited:
                result.append(cell)

        return result







