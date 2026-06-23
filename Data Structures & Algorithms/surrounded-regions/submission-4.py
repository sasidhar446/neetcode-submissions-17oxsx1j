class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != 'O':
                return
            board[r][c] = '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(dr + r, dc + c)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        

        
        