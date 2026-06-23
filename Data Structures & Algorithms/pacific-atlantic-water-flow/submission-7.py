class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_set, atlantic_set, pacific_deq, atlantic_deq = set(), set(), deque(), deque()

        rows, cols, result = len(heights), len(heights[0]), []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_deq.append((r, c))
                if r == rows - 1 or c == cols -1:
                    atlantic_deq.append((r, c))
        
        def bfs(deq_, set_):
            while deq_:
                r, c = deq_.popleft()
                if (r, c) in set_:
                    continue
                set_.add((r, c))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                        deq_.append((nr, nc))
        
        bfs(pacific_deq, pacific_set)
        bfs(atlantic_deq, atlantic_set)

        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                result.append([r, c])
        
        return result

                        
        
