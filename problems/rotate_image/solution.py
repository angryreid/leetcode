class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # for i in range(n // 2):
        #     for j in range(i, n - 1 - i):
        #         t = matrix[i][j]
        #         matrix[i][j] = matrix[n - 1 - j][i]
        #         matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
        #         matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        #         matrix[j][n - 1 - i] = t

        n = len(matrix)
        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
        
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
