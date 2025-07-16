class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [0] * n
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == row - i:
                    return False
            return True
        
        def backtrack(board, row):
            if row == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
        backtrack(board, 0)
        return res