class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False

        rows, cols = len(board), len(board[0])

        def hasWord(r, c, index):
            if board[r][c] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            board[r][c] = '#'
            
            for dr, dn in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = dr + r, dn + c

                if 0 <= nr < rows and 0 <= nc < cols:
                    if hasWord(nr, nc, index + 1):
                        return True
            
            board[r][c] = word[index]

            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if hasWord(r, c, 0):
                        return True
        
        return False
