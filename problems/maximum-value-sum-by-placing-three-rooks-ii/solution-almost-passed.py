from typing import List
# 803 / 857 testcases passed
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n = len(board)  # Number of rows
        m = len(board[0])  # Number of columns
        max_sum = float('-inf')  # Initialize max_sum to negative infinity

        # Helper function for backtracking
        def backtrack(row: int, col_mask: int, count: int, current_sum: int):
            nonlocal max_sum
            
            # If we have placed 3 rooks, update max_sum
            if count == 3:
                max_sum = max(max_sum, current_sum)
                return
            
            # If we have gone through all rows, return
            if row >= n:
                return
            
            # Try placing a rook in the current row
            for col in range(m):
                # Check if the column is already used
                if (col_mask & (1 << col)) == 0:
                    # Place the rook and move to the next row
                    backtrack(row + 1, col_mask | (1 << col), count + 1, current_sum + board[row][col])
            
            # Also consider not placing a rook in the current row
            backtrack(row + 1, col_mask, count, current_sum)

        # Start backtracking from the first row
        backtrack(0, 0, 0, 0)
        
        return max_sum if max_sum != float('-inf') else -1  # Return -1 if no valid placement found