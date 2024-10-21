class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == row - i:
                    return False
            return True

        def solve_n_queens_util(board, row):
            if row == n:
                solutions.append(["." * i + "Q" + "." * (n - i - 1) for i in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve_n_queens_util(board, row + 1)

        solutions = []
        board = [0] * n
        solve_n_queens_util(board, 0)
        return solutions
        