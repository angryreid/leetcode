from typing import List

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        # Get the number of rows and columns
        m = len(board)
        n = len(board[0]) if board else 0  # Handle the case where the board is empty
        if m == 0 or n == 0:  # Handle the case where the board is empty
            return 0
        
        self.maxn = float('-inf')  # Correct initialization of maxn
        
        # Function to check if placing a piece at (row, col) is valid
        def is_valid(places: List[List[int]], row: int, col: int) -> bool:
            # Check if the column is already occupied by a rook
            for i in range(row):
                if places[i][col] == 1:  # Check the same column
                    return False
            return True

        # Recursive function to find the maximum value sum
        def max_value(places: List[List[int]], row: int, rook_count: int) -> None:
            # If we have placed exactly 3 rooks, calculate the sum
            if rook_count == 3:
                ans = 0
                for i in range(m):
                    for j in range(n):
                        if places[i][j] == 1:
                            ans += board[i][j]
                self.maxn = max(self.maxn, ans)  # Update the maximum value found
                return
            
            # If we are out of rows and haven't placed 3 rooks, return
            if row == m:
                return
            
            for col in range(n):  # Try placing a piece in each column
                if is_valid(places, row, col):
                    places[row][col] = 1  # Place a rook
                    max_value(places, row + 1, rook_count + 1)  # Move to the next row, with one more rook
                    places[row][col] = 0  # Backtrack
            
            # Explore the case where we skip placing a rook in the current row
            max_value(places, row + 1, rook_count)  # Move to the next row without placing a rook

        places = [[0] * n for _ in range(m)]  # Initialize places
        max_value(places, 0, 0)  # Start from the first row with 0 rooks placed
        return self.maxn  # Return the maximum value found