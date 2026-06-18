class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited, atlantic_visited = set(), set()
        rows, cols, result = len(heights), len(heights[0]), []

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    dfs(nr, nc, visited)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    dfs(r, c, pacific_visited)
                if r == rows - 1 or c == cols - 1:
                    dfs(r, c, atlantic_visited)


        for cell in atlantic_visited:
            if cell in pacific_visited:
                result.append(cell)

        return result
