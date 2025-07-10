class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [0] * n
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == row - i:
                    return False
            return True
        def solve_n_queen(board, row):
            if row == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve_n_queen(board, row + 1)
        
        solve_n_queen(board, 0)
        return res
                