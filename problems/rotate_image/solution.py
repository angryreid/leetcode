class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                t = matrix[i][j]
                # left top
                matrix[i][j] = matrix[n - j - 1][i]
                # left bottom
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                # right bottom
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                # right top
                matrix[j][n - i - 1] = t
